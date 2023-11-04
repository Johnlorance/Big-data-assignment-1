import pandas as pd

# Load the dataset (assuming you have already loaded it)

# Data Cleaning
# Task 1: Remove duplicate rows
df = df.drop_duplicates()

# Task 2: Handle missing values (replace with zeros for simplicity)
df.fillna(0, inplace=True)

# Data Transformation
# Task 3: Convert a column to uppercase 
df['Country'] = df['Country'].str.upper()

# Task 4: Calculate a new column from existing data 
df['Region_Length'] = df['Region'].apply(len)

# Data Reduction
# Task 5: Select a subset of columns
df = df[['Country', 'Region']]

# Task 6: Filter rows based on a condition
df = df[df['Region'].str.contains('Asia')]

# Data Encoding 
# Task 7: Encode categorical data into numerical values 

unique_countries = df['Country'].unique()
country_to_numeric = {country: idx for idx, country in enumerate(unique_countries)}
df['Country_Label'] = df['Country'].map(country_to_numeric)

# Task 8: Create a new column that combines 'Country' and 'Region'
df['Country_Region'] = df['Country'] + ' - ' + df['Region']
df.to_csv('/app/res_dpre.csv', index=False)

exec(open("app/eda.py").read())
