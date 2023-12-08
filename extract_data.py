import pandas as pd

# Load the CSV data into a Pandas DataFrame
df = pd.read_csv('Popular_Baby_Names.csv')

# Filter out rows where 'Count' is zero or null
df_filtered = df[df['Count'].notna() & (df['Count'] > 0)]

# Combine data for 'WHITE NON HISP' and 'WHITE NON HISPANIC' into one column
df_filtered['Ethnicity'] = df_filtered['Ethnicity'].replace({'WHITE NON HISP': 'WHITE', 'WHITE NON HISPANIC': 'WHITE'})

df_filtered['Ethnicity'] = df_filtered['Ethnicity'].replace({'BLACK NON HISP': 'BLACK', 'BLACK NON HISPANIC': 'BLACK'})

# Group data by 'Ethnicity' and sum the 'Count' for each name
ethnicity_trends = df_filtered.groupby(['Ethnicity', 'Child\'s First Name'])['Count'].sum().unstack()

# Replace NaN values with 'X'
ethnicity_trends = ethnicity_trends.fillna('X')

# Save the modified DataFrame to a new CSV file
ethnicity_trends.to_csv('filtered_ethnicity_trends_combined.csv', index=True)

print("Naming Trends Among Different Ethnicities (Combined and Filtered CSV saved as 'filtered_ethnicity_trends_combined.csv'):")
print(ethnicity_trends)
