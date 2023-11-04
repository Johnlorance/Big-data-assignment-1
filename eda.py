import pandas as pd

# Load the preprocessed dataset (assuming you have already loaded it)

# Exploratory Data Analysis (EDA) without visualizations
# Insight 1: Calculate the average population
unique_regions = df['Region'].nunique()
insight1 = f"Insight 2: There are {unique_regions} unique regions in the dataset."

# Insight 2: Find the most common region
most_common_region = df['Region'].mode().iloc[0]
insight2 = f"Insight 2: The most common region is '{most_common_region}'."

# Insight 3: Calculate the total number of countries
total_countries = len(df)
insight3 = f"Insight 3: There are {total_countries} countries in the dataset."

# Save insights as text files
with open('/app/eda-insight-1.txt', 'w') as file:
    file.write(insight1)

with open('/app/eda-insight-2.txt', 'w') as file:
    file.write(insight2)

with open('/app/eda-insight-3.txt', 'w') as file:
    file.write(insight3)

exec(open("app/vis.py").read())