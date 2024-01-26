import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("filtered_file.csv")

countries = data["Country"]
midwives = data["Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE"]

plt.figure(figsize=(20, 6))
plt.bar(countries, midwives, color='m')
plt.xlabel('Country (In Alphabetical Order)', fontsize=15)
plt.ylabel('Number of Midwives per 10,000 Population', fontsize=15)
plt.title('Number of Midwives by Country', fontsize=15)
plt.grid(axis='y')
plt.xticks(rotation=90)
y_ticks = range(0, int(max(midwives)) + 50, 25)
plt.yticks(y_ticks)
plt.savefig('midwives.png', bbox_inches='tight')
