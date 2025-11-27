import pandas as pd
data={
    "Name":["jack","joe","jonh","james"],
    "age":[23,24,22,25],
    "city":["delhi","varanasi","noida","greater noida"]
}

df=pd.DataFrame(data)

print("\n",df.iloc[0])
print("\n",df.iloc[1])
print("\n",df.iloc[2])

print("--------------------")

print("\n",df.loc[[0,2]])

print("\n",df.loc[2,"city"])