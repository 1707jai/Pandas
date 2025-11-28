import pandas as pd

data={
    "Name":["jack","john","joe","Jr"],
    "age":[23,22,25,21],
    "city":["paris","New york city","London","tokyo"]
}
df=pd.DataFrame(data)


df.loc[2,"age"]=27
df.loc[3,"city"]="delhi"

print(df.iloc[2])
print(df.iloc[3])