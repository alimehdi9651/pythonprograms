import pandas as pd 
data = {
    "Name" :['ali', 'mehdi', ' rizvi'],
    "Age" : [18, 22, 14],
    "City" : ['Lucknow', 'Mumbai', 'Delhi']
}
df = pd.DataFrame(data)
# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)

# print(df)