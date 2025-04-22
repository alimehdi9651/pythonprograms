import pandas as pd
# customer_data = pd.DataFrame({
#     "Name" : ["ali", "mehdi", "abbas"],
#     "Customer_id": [1,2,3]
# })
# order_data =  pd.DataFrame({
#     "Amount" : [100, 200,500],
#     "Customer_id": [2,3,4]
# })
#Merging take place through the common colums present in both the table just like SQL
#we use merge(left_dataframe or dataframe1, rigth_dataframe or dataframe2, on = "colum_name_on_which_we_want_merge_our_dataFrame", how="type of merging")
# it has 5 types
#1). Inner join: it return the data on the basis of common data present in the common colum
# inner_merge = pd.merge(customer_data, order_data, on="Customer_id", how="inner")
# print(inner_merge)
# #2). outer join: it return the complete data and if some cells are not present then it will fill NOne or NaN
# outer_merge = pd.merge(customer_data, order_data, on="Customer_id", how="outer")
# print(outer_merge)
# #3). left join: it return the data present on the left dataFrame
# left_merge = pd.merge(customer_data, order_data, on="Customer_id", how="left")
# print(left_merge)
# #4). right : reverse of left join
# right_merge = pd.merge(customer_data, order_data, on="Customer_id", how="right")
# print(right_merge)
# #5). Cross jion: nahi pata bhai
# cross_merge = pd.merge(customer_data, order_data, how="cross")
# print(cross_merge)






#Concatinate of dataFrames
#using concat([List of dataFrames seperate by commas], axis=0 for verically concatination/1 for horixontally concatination, ignore_index=True/ index will be setted 0 after concatination)
df1 = pd.DataFrame({
    "Coustomer_id" : [1,2,3],
    "Name": ["Ali", "Mehd", "abbas"]
})
df2 = pd.DataFrame({
    "Coustomer_id" : [4,5,6],
    "Name": ["ayush", "ahmed", "abhishek"]
})

concatinated_dataFrame = pd.concat([df1,df2], axis=0, ignore_index=True)
print(concatinated_dataFrame)