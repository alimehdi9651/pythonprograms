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
dataset = df[(df['Salary'] > 55000) & ((df['Age'] > 25) | (df['Performance'] > 95))]
print(dataset)