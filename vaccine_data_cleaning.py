import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"/Users/alexanderbrost/Desktop/root/py/covid-19/vaxage.csv")

# Filter for counties in 7-co (from respnetage)

counties = [
    'ANOKA', 'CARVER', 'DAKOTA', 'HENNEPIN', 'RAMSEY', 'SCOTT', 'WASHINGTON'
]

data_filtered = data[data["County"].isin(counties)]

# Remove non-covid data

data_filtered = data_filtered.drop("People up to date on influenza vaccinations", axis=1)
data_filtered = data_filtered.drop("Percent up to date on influenza vaccinations", axis=1)
data_filtered = data_filtered.drop("Percent up to date", axis=1)
data_filtered = data_filtered.drop("People up to date", axis=1)

# New .csv with cleaned dataset

data_filtered.to_csv("/Users/alexanderbrost/Desktop/root/py/covid-19/vaxage_clean.csv")

# New df from new .csv to combine data

df = pd.read_csv(r"/Users/alexanderbrost/Desktop/root/py/covid-19/vaxage_clean.csv")

df = df.drop("County", axis=1)
df = df.drop("reportedDate", axis=1)
df = df.drop("webDate", axis=1)

# Group data by age group & sum 

grouped_data = df.groupby("Age Group").apply(
    lambda x: (x['Percent up to date on COVID-19 vaccinations'] * x['People up to date on COVID-19 vaccinations']).sum() / x['People up to date on COVID-19 vaccinations'].sum()
).reset_index(name='weighted_average_percentage')

# New df with Weighted Averages

grouped_data.to_csv(r"/Users/alexanderbrost/Desktop/root/py/covid-19/vaxage_clean_weighted.csv")
