import pandas as pd

my_df = pd.read_csv("student.csv")

#chatgpt.com helped me create the dataframe
filtered_df = my_df[(my_df["studytime"] >= 3) & (my_df["internet"] ==1) & (my_df["absences"] <=5)]
filtered_df.to_csv("high_engagement.csv", index=False)

number_of_students = len(filtered_df)

print("Number saved", number_of_students)

average_grade = filtered_df["grade"].mean()
print("Average grade: ", average_grade)