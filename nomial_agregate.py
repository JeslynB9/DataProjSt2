import pandas as pd
import matplotlib.pyplot as plt

# Import CSV file
data = pd.read_csv('filtered_file.csv') 

# Calculate the median number of midwives for each region
median_midwives = data.groupby('Region')['Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE'].median().reset_index().round(2)

# Sort the DataFrame by the median number of midwives in descending order
median_midwives = median_midwives.sort_values(by='Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE', ascending=False)

# Create a table using Matplotlib
fig, ax = plt.subplots(figsize=(6, 2))

# Hide axes
ax.axis("off")

# Add a title to the table and adjust the position and padding
title = ax.set_title('Median Number of Midwives per 10,000 Population by Region', fontsize=10, y=1)

# Create a table and add it to the axis
table = ax.table(cellText=median_midwives.values, colLabels=['Region', 'Median Number of Midwives per 10,000 Population'], cellLoc="center", loc="center")

# Customize table appearance
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)  # Adjust the table size as needed
table.auto_set_column_width([0, 1])

# Save the table as a PNG image
plt.savefig('median_midwives_table.png', bbox_inches='tight', pad_inches=0.1, dpi=300)


