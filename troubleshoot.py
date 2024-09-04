import pandas as pd
import requests

# Load the list of websites
websites_df = pd.read_csv(r"D:\University of York\Assessments\PCYB\Python\concatenated_unique_websites.csv")

# Function to check if a website is active using a GET request
def is_website_active(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Initialize a counter
total_websites = len(websites_df)
print(f"Total websites to check: {total_websites}")

# Add a new column to indicate if the website is active
active_status = []
for index, row in websites_df.iterrows():
    domain = row['Domain Name']
    is_active = is_website_active(f"http://{domain}")
    active_status.append(is_active)
    print(f"Processing {index + 1}/{total_websites}: {domain} - {'Active' if is_active else 'Inactive'}")

# Assign the active status to the DataFrame
websites_df['Is Active'] = active_status

# Save the updated list to a new CSV file
websites_df.to_csv(r"D:\University of York\Assessments\PCYB\Python\verified_websites.csv", index=False)

print("Verification completed. Check the 'Is Active' column in the CSV file.")
