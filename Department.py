import pandas as pd

data={
    "Name":["Emma","Olivia","liam","Noah","Sophia","james","Ava","Lucas"],
    "Age":[28,32,26,45,30,38,27,41],
    "Department":["IT","Finance","IT","HR","Marketing","Finance","HR","IT"],
    "Salary":[70000,85000,65000,90000,72000,95000,68000,88000],
    "Experience":[3,7,2,10,4,12,3,9]

}

df=pd.DataFrame(data)

print(df)

print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Salary"].min())
print(df.groupby("Department")["Salary"].sum())

high=df[df["Salary"]>70000]
print(high.groupby("Department")["Salary"].mean())