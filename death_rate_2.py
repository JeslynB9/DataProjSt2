import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("filtered_file.csv")

grouped_data = data.groupby("Country", as_index=False).mean(numeric_only=True)

countries = grouped_data["Country"]
columns = ["Neonatal mortality rate (deaths per 1,000 live births)",
            "Infant mortality rate (deaths per 1,000 live births):::BOTHSEX"]

x = np.arange(len(countries))
bar_width = 0.4 

colors = ['c', 'm']

plt.figure(figsize=(20, 8))
labels = ["Neonatal Norality Rate", "Infant Mortality Ratio"]

for i, column in enumerate(columns):
    plt.bar(x + i * bar_width, grouped_data[column], bar_width, label=labels[i], color=colors[i])

plt.xlabel('Country (In Alphabetical Order)', fontsize=20)
plt.ylabel('Mortality Rate per 1,000 Live Births', fontsize=20)
plt.title('Neonatal and Infant Deaths by Country', fontsize=20)
plt.legend()
plt.grid(True)

plt.xticks(x + bar_width * (len(columns) - 1) / 2, countries, rotation=90)
plt.tight_layout()
plt.savefig('death_rate2.png', bbox_inches='tight')

