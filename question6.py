import pandas as pd

my_df = pd.read_csv("crime.csv")

my_df["risk"] = my_df["ViolentCrimesPerPop"].apply(lambda x: "HighCrime" if x >=0.5 else "LowCrime")
grouped_things = my_df.groupby("risk")["PctUnemployed"].mean()

for i in ["HighCrime", "LowCrime"]:
    print(f"Average unemployed rate for {i}: {grouped_things[i]}")