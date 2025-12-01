import pandas as pd
data={
    "Name":["jack","john","jully","jemi"],
    "age":[24,23,22,21],
    "city":["New York","Los Angeles","phoenix","San francisco"],
    "salary":[30000,32000,30000,31500]
}

df=pd.DataFrame(data)


#print(df)

#row print
#print(df.loc[0])

#add new data 
#print(df)

high_salary=df[df["salary"] >=31000 ]
print(high_salary)

