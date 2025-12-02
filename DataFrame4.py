import pandas as pd

data = {
    "Name": ["John", "Emma", "Oliver", "Sophia", "Liam", "Ava", "Noah", "Mia", "James", "Isabella",
             "Elijah", "Amelia", "William", "Charlotte", "Benjamin", "Harper", "Lucas", "Evelyn", "Henry", "Abigail"],

    "Age": [25, 30, 22, 28, 35, 26, 24, 33, 31, 27,
            29, 23, 34, 32, 36, 21, 40, 38, 37, 20],

    "City": ["New York", "London", "Sydney", "Berlin", "Toronto", "Paris", "Dubai", "Rome", "Madrid", "Chicago",
             "Tokyo", "Amsterdam", "Seoul", "Zurich", "Los Angeles", "Barcelona", "Singapore", "Vienna", "Istanbul", "Stockholm"],

    "Salary": [80000, 92000, 75000, 68000, 120000, 95000, 70000, 88000, 99000, 66000,
               72000, 54000, 130000, 110000, 85000, 50000, 140000, 125000, 76000, 48000]
}

df = pd.DataFrame(data)
print(df)


print(df[df["Salary"] > 70000])
mean_salary=df["Salary"].mean()
median_salary=df["Salary"].median()
std_salary=df["Salary"].std()
var_salary=df["Salary"].var()

print("\n",mean_salary,"\n",median_salary,"\n",std_salary,"\n",var_salary)