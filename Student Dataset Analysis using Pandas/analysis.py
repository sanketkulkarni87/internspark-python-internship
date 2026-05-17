import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

print("=== Original Data ===")
print(df)



# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()


print("\nStudents with Marks > 80:")
high_scorers = df[df["Marks"] > 80]
print(high_scorers)



print("\nAverage marks by Department:")
grouped = df.groupby("Department")["Marks"].mean()
print(grouped)



print("\nInsights:")
print("1. Highest marks:", df["Marks"].max())
print("2. Lowest marks:", df["Marks"].min())
print("3. Average marks:", df["Marks"].mean())



grouped.plot(kind="bar")
plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.show()