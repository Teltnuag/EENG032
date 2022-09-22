## Week 2 Lesson 4
import pandas as pd
import matplotlib.pyplot as plt

deathRates = pd.read_csv('Compressed Mortality, 1999-2015 Archive.csv', delimiter='\t')
deathRates.loc[deathRates["Crude Rate"]=="0.0 (Unreliable)","Crude Rate"] = 0.0
deathRates["Crude Rate"] = deathRates["Crude Rate"].astype("float64")
plot = deathRates[deathRates["Notes"] == "Total"][["Year","Crude Rate"]]
plt.plot(plot.Year, plot["Crude Rate"])
plt.show()

temp = pd.read_json("Global Temperature Anomaly 1880-2016.json")
plt.plot(temp)
plt.show()