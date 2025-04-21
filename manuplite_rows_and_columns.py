import pandas as pd 
data = {
    "Name": ["Ali", "Mehdi", "Sara", "John", "Ayesha", "Ravi", "Neha", "Zaid", "Priya", "Rahul"],
    "Salary": [50000, 55000, 47000, 60000, 53000, 52000, 48000, 58000, 49000, 51000],
    "Age": [25, 26, 24, 30, 27, 28, 23, 29, 26, 25],
    "Performance": [88, 95, 76, 98, 85, 82, 74, 91, 79, 80]
}
df = pd.DataFrame(data)
# selecting specific rows
# let select name colum
# name = df["Name"]
# print(name)
# selecting multiple colmns
# subset = df[["Name", "Age"]]
# print(subset)


# filtering rows for the dataFrame on the basis of some conditions

# highSalary = df[df["Salary"] > 50000]
# print("people having salary more than 50000")
# print(highSalary)

#filtering rows for the dataFrame on the basis of multiple conditions based on AND

# dataset = df[(df["Salary"] > 55000) & (df['Age'] > 26)]
# print(dataset)

#Multiple Condition based on OR
# dataset = df[(df['Salary'] > 55000) & ((df['Age'] > 25) | (df['Performance'] > 95))]
# print(dataset)





# adding new colum to the dataset
#1. Straigt forward or direct placement 
# this method place the created colum at the very last index.
# print(df)

# df['Bonus'] = df['Salary'] * 0.1
# # print(df)

# print(df)

#2. using insert() method
# it help us to place the colum to a particular index
#df.insert(index, col_name, [data])
# df.insert(0, " Employee_Id", [201,202,203,204,205,206,207,208,209,2010])
# print(df)


#--------------------------------------------------------------------------------------------------------------------

#Updating a particular cell using loc() method
# let change the salary of ayesha from 53000 to 100000
#.loc(index of target row, colum name )
# df.loc[4, 'Salary'] =  100000
# print(df)
# # using loc() method we can change or update any particular cell.


# # Updating complete colum 
# df["Salary"] = df["Salary"] * 1.02
# print(df)



#Deleting or droping an unused coloum using drop() method
# print(df)
# df.drop(columns= ["Performance", 'Age'], inplace=True) # we can delete multiple colmn by seprating there names through commos
# print(df)
 

#Data cleaning 
#Finding null values
#using isnull() function

data2 = {
    "Name": ["Ali", None, "Sara", "John", "Ayesha", "Ravi", "Neha", "Zaid", "Priya", "Rahul"],
    "Salary": [50000, None, 47000, 60000, 53000, 52000, 48000, 58000, 49000, 51000],
    "Age": [25, None, 24, 30, 27, 28, 23, 29, 26, 25],
    "Performance": [88, None, 76, 98, 85, 82, 74, 91, 79, 80]
}
df2 = pd.DataFrame(data2)
# print(df2.isnull())
#if want to find how many cells are not filed
# print(df2.isnull().sum())

print(df2)
#Filling or handling and removing  missing values

#if those missing are not useful we can simply drop or delete that none data
#usning dropna() function
df2.dropna(inplace=True)
print(df2)

#using this dropna() we can simply delete the None Row
# or None data
