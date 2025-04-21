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
    "Name": ["Ali", 'Mehdi', "Sara", "John", "Ayesha", "Ravi", "Neha", "Zaid", "Priya", "Rahul"],
    "Salary": [50000, 52000, 47000, 60000, 53000, 52000, 48000, 58000, 49000, 51000],
    "Age": [23, 24, 24, 30, 27, 30, 23, 30, 26, 26],
    "Performance": [88, 80, 76, 98, 85, 82, 74, 91, 79, 80]
}
df2 = pd.DataFrame(data2)
# print(df2.isnull())
#if want to find how many cells are not filed
# print(df2.isnull().sum())

print(df2)
#Filling or handling and removing  missing values

#if those missing are not useful we can simply drop or delete that none data
#usning dropna() function
# df2.dropna(inplace=True)
# print(df2)

#using this dropna() we can simply delete the None Row
# or None data


#if you want to fill some data at None or NaN then we use fillna(value , inplace = true)
#here value will bw replace with None or NaN

# df2.fillna(0, inplace=True) 
# #here none and nan gonna fill with 0, we can use this if we want to fill some default value in it.
# print(df2)


# if we want to fill some useful data at none then we have to target a particular row
#we have two options 
# df2['Age'].fillna(df2["Age"].mean(), inplace=True)

# df2["Age"] = df2['Age'].fillna(df2["Age"].mean()) # preffered one
# df2["Salary"] = df2['Salary'].fillna(df2["Salary"].mean())
# print(df2)





#Interpolation : if we want to get some meaning full data at the place on None 
# then we use interpolation, it put some mathamatically calculated value, based on previous data present in the series, at the place of None 
#using interpolate(mehtod="", axis = 0), inplace = true: here method can be linear, polynomial or time 
# df2["Salary"] = df2["Salary"].interpolate(method="linear")
# # print(df2)
# dates = pd.date_range(start='2025-01-01', periods=6, freq='D')
# print(dates)




#Aggregation and sorting
# df2.sort_values(by = "Salary", ascending=True, inplace=True)
# print(df2)


#if you want to sort multiple rows
# then pass list in by and assending arguments of sort_values
# df2.sort_values(by = ["Age", "Salary"], ascending=[True, True], inplace=True)
# print(df2)



#Aggregation refers to the specific calculation throughout the colum
#it can be mean() sum() avg() and many more
# avg_salary = df2["Salary"].mean()
# avg_salary = df2["Salary"].sum()
# print(avg_salary)



#Grouping in pandas
#we can group similar data for future aggrigation, where grouing help us to find the sum(), count(), mean(),  min() , std()
# and many more such operation on those similar data or values present in dataFrame
# group = df2.groupby("Age")["Salary"].max()
# print(group)
#We can group multiple colum data just by adding colum name
groups = df2.groupby(["Age", "Name"])["Salary"].max()
print(groups)