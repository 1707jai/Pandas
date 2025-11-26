import pandas as pd

arr=pd.Series([10,20,30,40,50])
data={
    "Name":["jai","jack","jackson","joe"],
    "age":[24,23,22,23],
    "city":["varanasi","delhi","banaras","noida"]
}

df=pd.DataFrame(data)
print(df)

print("\n",df.Name)
#print("\n",df["age"])

