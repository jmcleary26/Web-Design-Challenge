import pandas as pd
# Process of generating HTML table from a pandas dataframe

# Read in csv containing city data
web_data = pd.read_csv('Resources/cities.csv')

# Save to file
web_data.to_html('data.html', index=False)

# Assign to string and print results
table = web_data.to_html()
print(table)