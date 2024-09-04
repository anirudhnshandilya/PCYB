import ssl
import socket
import OpenSSL
from urllib.parse import urlparse
import logging
import os
import pandas as pd
from datetime import datetime

# Configure logging to display messages in the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def format_date(date_str):
    # Convert the date string from the certificate to a datetime object
    date_obj = datetime.strptime(date_str, '%Y%m%d%H%M%SZ')
    # Return only the date in the format 'Day Month Year'
    return date_obj.strftime('%d %B %Y')

def get_certificate_info(hostname):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)

    try:
        # Connect to the server
        conn.connect((hostname, 443))

        # Get the certificate
        cert = conn.getpeercert(True)
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert)

        # Extracting details
        issuer = x509.get_issuer()
        issuer_cn = issuer.CN if issuer.CN else 'Unknown'
        validity_start = format_date(x509.get_notBefore().decode('utf-8'))
        validity_end = format_date(x509.get_notAfter().decode('utf-8'))
        sha256_fingerprint = x509.digest('sha256').decode('utf-8')
        cert_length = len(cert)
        public_key = x509.get_pubkey()
        public_key_length = public_key.bits()

        # Check secure connection and encryption/authentication
        secure_connection = True if conn.version() else False
        encryption = conn.cipher() if conn.cipher() else ('Unknown', 'Unknown', 'Unknown')

        return {
            "issuer": issuer_cn,
            "validity_start": validity_start,
            "validity_end": validity_end,
            "sha256_fingerprint": sha256_fingerprint,
            "cert_length": cert_length,
            "public_key_length": public_key_length,
            "secure_connection": secure_connection,
            "encryption": encryption,
            "error": ""
        }
    except ssl.SSLError as e:
        error_message = f"SSL error: {str(e)}"
        logging.error(f"Error processing {hostname}: {error_message}")
        return {
            "issuer": "",
            "validity_start": "",
            "validity_end": "",
            "sha256_fingerprint": "",
            "cert_length": "",
            "public_key_length": "",
            "secure_connection": "",
            "encryption": "",
            "error": error_message
        }
    except socket.error as e:
        error_message = f"Socket error: {str(e)}"
        logging.error(f"Error processing {hostname}: {error_message}")
        return {
            "issuer": "",
            "validity_start": "",
            "validity_end": "",
            "sha256_fingerprint": "",
            "cert_length": "",
            "public_key_length": "",
            "secure_connection": "",
            "encryption": "",
            "error": error_message
        }
    except Exception as e:
        error_message = f"General error: {str(e)}"
        logging.error(f"Error processing {hostname}: {error_message}")
        return {
            "issuer": "",
            "validity_start": "",
            "validity_end": "",
            "sha256_fingerprint": "",
            "cert_length": "",
            "public_key_length": "",
            "secure_connection": "",
            "encryption": "",
            "error": error_message
        }
    finally:
        conn.close()

def process_websites_from_csv(csv_file_path, output_csv_file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Log the columns to check what is available
    logging.info(f"Columns in the CSV file: {df.columns.tolist()}")

    # Use the correct column names from the CSV
    website_column = 'Domain Name'  # The column with domain names
    category_column = 'Category'  # The column with categories

    websites = df[website_column].tolist()
    categories = df[category_column].tolist()

    results = []
    for idx, (website, category) in enumerate(zip(websites, categories), start=1):
        logging.info(f"Processing website {idx}/{len(websites)}: {website}")
        parsed_url = urlparse(f"https://{website}")
        hostname = parsed_url.hostname

        info = get_certificate_info(hostname)
        info['website'] = website
        info['category'] = category  # Include the category in the results
        results.append(info)

    output_df = pd.DataFrame(results)

    # Save the results to a CSV file
    output_df.to_csv(output_csv_file_path, index=False)
    logging.info(f"Processing complete. Results saved to {output_csv_file_path}.")

    return output_df

if __name__ == "__main__":
    # Define the paths to your input and output CSV files
    csv_file_path = r"D:\University of York\Assessments\PCYB\Python\concatenated_unique_websites.csv"
    output_csv_file_path = r"C:\Users\aniru\Downloads\ezz1.csv"

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_csv_file_path), exist_ok=True)

    # Process the websites and save the results to a CSV file
    df_result = process_websites_from_csv(csv_file_path, output_csv_file_path)
    print(df_result.head())
