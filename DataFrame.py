import pandas as pd
data={
"Name":["Aman","Siya","jack"],
"age":[21,22,20],
"city":["delhi","mumbai","texas"]
}

df=pd.DataFrame(data)
print(df)
print("----------------------")

data={
    "Product":["laptop","phone","tablet"],
    "price":[60000,30000,20000],
    "Qty":[2,5,3]
}

new=pd.DataFrame(data)
print(new)