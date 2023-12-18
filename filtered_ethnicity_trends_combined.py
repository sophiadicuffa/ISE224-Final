import pandas as pd


# Load the CSV data into a Pandas DataFrame

baby_names = pd.read_csv('Popular_Baby_Names.csv')


# Checking for missing values

missing_values = baby_names.isnull().sum()


# Checking for duplicate entries

duplicate_entries = baby_names.duplicated().sum()


# Checking for data types and potential inconsistencies

data_types = baby_names.dtypes


# Overview of the dataset's basic statistics

basic_stats = baby_names.describe()


# Removing duplicate entries

baby_names_cleaned = baby_names.drop_duplicates()


# Data Normalization: Standardizing text fields (capitalization)

baby_names_cleaned['Gender'] = baby_names_cleaned['Gender'].str.title()

baby_names_cleaned['Ethnicity'] = baby_names_cleaned['Ethnicity'].str.title()

baby_names_cleaned["Child's First Name"] = baby_names_cleaned["Child's First Name"].str.title()


# Rechecking for duplicates after normalization (in case casing caused perceived duplicates)

duplicate_entries_after_normalization = baby_names_cleaned.duplicated().sum()


# Displaying a few rows of the cleaned data for verification

cleaned_data_preview = baby_names_cleaned.head()


# Filter out rows where 'Count' is zero or null

baby_names_filtered = baby_names_cleaned[baby_names_cleaned['Count'].notna() & (
    baby_names_cleaned['Count'] > 0)]


# Combine data for 'WHITE NON HISP' and 'WHITE NON HISPANIC' into one column

baby_names_filtered['Ethnicity'] = baby_names_filtered['Ethnicity'].replace(
    {'WHITE NON HISP': 'WHITE', 'WHITE NON HISPANIC': 'WHITE'})

baby_names_filtered['Ethnicity'] = baby_names_filtered['Ethnicity'].replace(
    {'BLACK NON HISP': 'BLACK', 'BLACK NON HISPANIC': 'BLACK'})


# Group data by 'Ethnicity' and sum the 'Count' for each name

ethnicity_trends = baby_names_filtered.groupby(
    ['Ethnicity', "Child's First Name"])['Count'].sum().unstack()


# Replace NaN values with 'X'

ethnicity_trends = ethnicity_trends.fillna('X')


# Save the modified DataFrame to a new CSV file

ethnicity_trends.to_csv('filtered_ethnicity_trends_combined.csv', index=True)


print("Naming Trends Among Different Ethnicities (Combined and Filtered CSV saved as 'filtered_ethnicity_trends_combined.csv'):")

print(ethnicity_trends)


# Displaying additional information

print("\nMissing Values:")

print(missing_values)

print("\nDuplicate Entries:", duplicate_entries)

print("\nDuplicate Entries After Normalization:",
      duplicate_entries_after_normalization)

print("\nData Types:")

print(data_types)

print("\nBasic Statistics:")

print(basic_stats)

print("\nCleaned Data Preview:")

print(cleaned_data_preview)
