import pandas as pd
import matplotlib.pyplot as plt

# Load the original dataset
df = pd.read_csv('domains_without_errors.csv')

# Function to extract encryption details (same as before)
def extract_encryption_details(encryption_str):
    if isinstance(encryption_str, str):
        encryption_parts = encryption_str.replace('(', '').replace(')', '').split(', ')
        cipher_suite = encryption_parts[0]
        return cipher_suite
    return None

# Apply the function to create a new 'cipher_suite' column
df['cipher_suite'] = df['encryption'].apply(extract_encryption_details)

# Identify the top 10 categories by frequency
top_categories = df['category'].value_counts().head(10).index

# Filter the dataset to include only the top 10 categories
df_top_categories = df[df['category'].isin(top_categories)]

# Group by category and cipher_suite and count occurrences
cipher_suite_by_category = df_top_categories.groupby(['category', 'cipher_suite']).size().unstack(fill_value=0)

# Convert the counts to percentages by dividing by the total in each category
cipher_suite_by_category_percentage = cipher_suite_by_category.div(cipher_suite_by_category.sum(axis=1), axis=0) * 100

# Plotting the cipher suite trends by category as a stacked bar chart in percentages
plt.figure(figsize=(14, 8))
cipher_suite_by_category_percentage.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='Set3')

plt.title('Cipher Suite Trends by Top 10 Website Categories (in Percentages)')
plt.xlabel('Website Category')
plt.ylabel('Percentage of Websites')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Cipher Suite', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
