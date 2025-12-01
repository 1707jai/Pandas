import pandas as pd
data={
    "Name":["jack ","jones","jeniffer","jully"],
    "age":[23,32,21,22],
    "city":["miami","Las Vegas","San Francisco","phoenix"],
    "salary":[60000,65000,62000,61000]
}

df=pd.DataFrame(data)

print(df.loc[2])
print(df.loc[0])