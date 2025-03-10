import pandas as pd
import matplotlib.pyplot as plt

# Import CSVs

resp = pd.read_csv(r"/Users/alexanderbrost/Desktop/root/py/covid-19/respnetage_clean.csv")
vax = pd.read_csv(r"/Users/alexanderbrost/Desktop/root/py/covid-19/vaxage_clean_weighted.csv")

# Visualizing vax

x = vax["Age Group"]
y = vax["weighted_average_percentage"]

plt.plot(x, y)
plt.xlabel("Age Group")
plt.ylabel("Weighted Average")
plt.title("Weighted Average Percentages of COVID-19 Vaccinations by Age Group in 7-CO")
plt.show()

# Visualizing resp

plt.figure() 

columns = [
    "Season", "MMWR Startdate", "Pathogen", "geo", "index"
]
resp = resp.drop(columns=columns)
resp_grouped = resp.groupby("Age Group").sum()

a = resp_grouped.index
b = resp_grouped["Count of Hospitalizations"]

plt.plot(a, b)
plt.xlabel("Age Group")
plt.ylabel("Count of Hospitalizations")
plt.title("Count of Total Hospitalizations by Age Group")
plt.show()