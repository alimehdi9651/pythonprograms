import pandas as pd 
## METHODS IN PANDAS



df = pd.read_json("sample_Data.json")
# print('first 10 rows')
# print(df.head(10)) # by default it will return first 5 rows
# print('last 10 rows')
# print(df.tail(10))#by default it will return last 5 rows
# print(df)

#3. info():This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.


print(df.info())
data = {
    "Name" :['ali', 'mehdi', ' rizvi'],
    "Age" : [18, 22, 14],
    "City" : ['Lucknow', 'Mumbai', 'Delhi']
}

df1 = pd.DataFrame(data)
print(df1.info())


#4. describe(): The describe() function in pandas provides a quick statistical summary
#  (like count, mean, std, min, max, and percentiles) of all numeric columns in a DataFrame.
data2 = {
    "Name": ["Ali", "Mehdi", "Sara", "John", "Ayesha", "Ravi", "Neha", "Zaid", "Priya", "Rahul"],
    "Salary": [50000, 55000, 47000, 60000, 53000, 52000, 48000, 58000, 49000, 51000],
    "Age": [25, 26, 24, 30, 27, 28, 23, 29, 26, 25],
    "Performance": [88, 95, 76, 98, 85, 82, 74, 91, 79, 80]
}
df2 = pd.DataFrame(data2)
print(df2.describe())
print(df2)
#shape:its is an attribute that Return a tuple representing the dimensionality i.e (rows, columns)of the DataFrame. 
print(df2.shape)
#columns:it is an attribute that return the name of all the columns present in the data frame.
print(df2.columns)