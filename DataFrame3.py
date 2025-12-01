import pandas as pd
data={
    "Name":["jack ","jeniffer","jerry","Jr"],
    "age":[23,22,24,25],
    "city":["San Francisco","virginia","miami","colorado springs"],
    "salary":[50000,65000,60000,62000]
}

df=pd.DataFrame(data)

#print(df[df["age"] > 22 ])
print(df.query("age > 22"))
#print(df[df["salary"] < 63000 ])
print(df.query("salary > 63000"))

mean_salary=df["salary"].mean()

print(mean_salary)

median_salary=df["salary"].median()
print(median_salary)
