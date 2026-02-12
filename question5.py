import pandas as pd

my_df = pd.read_csv("student.csv")

def assign_band(grade):
    if grade <=9:
        return "Low"
    elif 10 <= grade and grade <= 14:
        return "Medium"
    else:
        return "High"

my_df["grade_band"] = my_df["grade"].apply(assign_band)

summary = my_df.groupby("grade_band").agg(
    number_of_students=("grade_band", "count"),
    average_absences=("absences", "mean"),
    internet_percentage=("internet", "mean")
)

summary["internet_percentage"] = summary["internet_percentage"] *100

summary.to_csv("student_bands.csv")
print(summary)