import pandas as pd
import matplotlib.pyplot as plt

# Load the provided dataset
data = pd.read_csv('filtered_file.csv')

# Define the midwives bins and labels
midwives_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ['0 - 10%', '10 - 20%', '20 - 30%', '30 - 40%', '40 - 50%', '50 - 60%', '60 - 70%', '70 - 80%', '80 - 90%', '90 - 100%']

# Create a new column to categorize data based on midwives bins
data['Midwives_Bin'] = pd.cut(data['Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE'], bins=midwives_bins, labels=labels, right=False)

# Calculate the average infant deaths and average neonatal deaths for each midwives bin
average_infant_deaths = data.groupby('Midwives_Bin')['Infant mortality rate (deaths per 1,000 live births):::BOTHSEX'].mean().reset_index()
average_neonatal_deaths = data.groupby('Midwives_Bin')['Neonatal mortality rate (deaths per 1,000 live births)'].mean().reset_index()

# Merge the two tables based on 'Midwives_Bin'
merged_table = pd.merge(average_infant_deaths, average_neonatal_deaths, on='Midwives_Bin')

# Format the values in the merged table to have two decimal places
merged_table['Infant mortality rate (deaths per 1,000 live births):::BOTHSEX'] = merged_table['Infant mortality rate (deaths per 1,000 live births):::BOTHSEX'].apply(lambda x: f'{x:.3f}')
merged_table['Neonatal mortality rate (deaths per 1,000 live births)'] = merged_table['Neonatal mortality rate (deaths per 1,000 live births)'].apply(lambda x: f'{x:.3f}')

# Create a table for the merged data
fig, ax = plt.subplots(figsize=(6, 2))
ax.axis("off")

# Title for the merged table
title_merged = ax.set_title('Average Infant and Neonatal Deaths for Different Midwives Ranges', fontsize=10, y=1.4)
table_merged = ax.table(cellText=merged_table.values, colLabels=['Midwives Bin', 'Avg Infant Deaths', 'Avg Neonatal Deaths'], cellLoc="center", loc="center")
table_merged.auto_set_font_size(False)
table_merged.set_fontsize(10)
table_merged.scale(1, 1.5)
table_merged.auto_set_column_width([0, 1, 2])

# Adjust the layout
plt.subplots_adjust(top=0.8)

# Save the merged table as a PNG
plt.savefig('merged_average_deaths.png', bbox_inches='tight', pad_inches=0.1, dpi=300)


