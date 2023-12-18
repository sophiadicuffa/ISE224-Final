import pandas as pd

import matplotlib.pyplot as plt


# Load the CSV data into a Pandas DataFrame

baby_names = pd.read_csv('Popular_Baby_Names.csv')


# Top 10 Most Popular Baby Names

top_10_names = baby_names['Child\'s First Name'].value_counts().head(10)

plt.figure(figsize=(10, 6))

top_10_names.plot(kind='bar', color='skyblue')

plt.title('Top 10 Most Popular Baby Names')

plt.xlabel('Names')

plt.ylabel('Frequency')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# Trend of the Name "Emma" Over the Years

emma_trend = baby_names[baby_names["Child's First Name"] == 'Emma']

emma_trend = emma_trend.groupby('Year of Birth')['Count'].sum()

plt.figure(figsize=(10, 6))

plt.plot(emma_trend.index, emma_trend.values, marker='o', color='orange')

plt.title('Trend of the Name "Emma" Over the Years')

plt.xlabel('Year')

plt.ylabel('Count')

plt.xticks(emma_trend.index, rotation=45)

plt.tight_layout()

plt.show()


# Distribution of Unique Names by Gender

unique_names_gender = baby_names.drop_duplicates(
    subset=["Child's First Name", 'Gender'])

gender_distribution = unique_names_gender['Gender'].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(gender_distribution, labels=gender_distribution.index,
        autopct='%1.1f%%', colors=['lightgreen', 'lightblue'])

plt.title('Distribution of Unique Names by Gender')

plt.tight_layout()

plt.show()
