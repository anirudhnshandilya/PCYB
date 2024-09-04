PCYB Repository
This repository contains a collection of datasets and Python scripts focused on analyzing various cryptographic and network security-related trends. Below is an overview of the files present in the repository, along with their respective descriptions:

Datasets (CSV Files)
Public_Key_Length_Distribution.csv
This file contains data on the distribution of public key lengths used in cryptographic certificates.

Raw Dataset.csv
The raw dataset with unprocessed data, likely containing a broad range of security-related information.

cipher_suite_trends.csv
Provides trends in cipher suite usage, including which cipher suites are most commonly used in SSL/TLS certificates.

cloudflare_processed.csv
This file contains processed data from Cloudflare, possibly related to network traffic or cryptographic usage.

cloudflare-radar-domains-top-100-20240815.csv
Contains data from Cloudflare Radar for the top 100 domains as of August 2024. This could include traffic statistics or SSL/TLS adoption rates for these domains.

concatenated_unique_websites.csv
A dataset with a list of unique websites that are aggregated or concatenated from other sources.

domains_with_errors.csv
This dataset lists domains that have encountered errors, possibly related to certificate misconfigurations or handshake failures.

domains_without_errors.csv
A dataset of domains that did not encounter any errors during the analysis.

key_size_distribution.csv
Data about the distribution of key sizes in SSL/TLS certificates across domains.

non_compliant_certificates.csv
This file contains information about certificates that are non-compliant with security standards.

tls_version_by_category.csv
Distribution of TLS (Transport Layer Security) versions used across different categories of websites.

tranco_J399Y.csv
Contains data from the Tranco list, which ranks domains based on popularity. This particular dataset is likely from a specific snapshot (e.g., J399Y version).

Python Scripts
main.py
The main Python script that orchestrates the analysis. It likely calls other scripts and processes the datasets mentioned above.

troubleshoot.py
A script intended to troubleshoot issues, likely related to SSL/TLS certificate analysis or data processing errors.

visualisations.py
This script generates visualizations based on the datasets, helping to provide insights on the trends and distributions.

Usage
Clone this repository:

bash
Copy code
git clone <repo-url>
Install any dependencies listed in requirements.txt (if applicable).

Run main.py to initiate the data analysis:

bash
Copy code
python main.py
Additional scripts like troubleshoot.py and visualisations.py can be used to perform specific tasks like debugging or generating graphs.

Contributions
Feel free to submit issues or pull requests if you find any problems or want to contribute to the project.
