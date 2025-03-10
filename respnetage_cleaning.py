import pandas as pd

data = pd.read_csv(r"/Users/alexanderbrost/Desktop/root/py/covid-19/respnetage_mn.csv")

# Remove irrelevant responses (only want) covid-19 data in 7-co

data_filtered = data[(data["Pathogen"] == "COVID-19") & (data["geo"] == "7-co")]
data_filtered = data_filtered.drop("population", axis=1) 
data_filtered = data_filtered.drop("MMWR Week", axis=1)

print(data_filtered)

# Checking for null values (no-null values found)

print(data_filtered.isnull().sum())

# Generating new .csv based on cleaned data

data_filtered.to_csv(r"/Users/alexanderbrost/Desktop/root/py/covid-19/respnetage_clean.csv")
