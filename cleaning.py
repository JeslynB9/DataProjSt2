import pandas as pd

data = pd.read_csv("SDG_goal3_clean.csv")
data = data[data["Year"] == 2010]

data.to_csv('filtered_file.csv', index=False)

