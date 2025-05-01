import numpy as np
# array = np.array([23.3, 40.2, 19.3, 24, 24.6])
# avg = array.mean()
# print(avg)



# want to create an array with some default values
# for default value 0
#zeros(shape of the array)
# arr = np.zeros(3) # this zero function create an array with 0 as default values
# arr = np.zeros((2,3))# this shape will give array of 2rows and 3 colums
# print(arr)

# if we want to fill 1 as default values
# one_arr = np.ones(3)

#if we want to fill a default value as per our need
# then use full((shape), value) function

# fill = np.full(3, 5)
# fill = np.full((2,3), 5)
# print(fill)



# want to create an array of a particular range
# use arange(start, stop, step): this function will return an numpy array

# arr = np.arange(1,11,1)
# print(arr)

# to print identity matrix
# use eye(shape)
# identity_matrix = np.eye(5)
# print(identity_matrix)



#Dimensions of array
# array = np.array([[2,3,4],[5,6,7]])
# print(array.shape)# this will give the (rows, columns) present in array
# print(array.size)# this will give the total number of element present in the array


# to check how many dimensions present in an array
# print(array.ndim)
# print(array.dtype)#this will give the data type o fthe array

# want to change data type od array from one to other
#use astype()
# arr = np.array([1.2,2.3,3.4]) # a float array
# print(arr.dtype)
# int_arr = arr.astype(int)
# print(int_arr, int_arr.dt) 




# modify elemets without using loops 

array = np.array([1,2,3,4,5,6])
# print(array + 5)# each element increase by 5 
# print(array * 5)
# print(array ** 2)
# print(array - 1)
# above operation modify our array without iteratibg each element


# Agregation function

# print(np.sum(array))


# print(np.min(array))
# print(np.mean(array))
# print(np.max(array))
# print(np.std(array))         
# print(np.var(array))
# print(type(array))

# array = np.array([1,2,3,4,5,6])
# #indexing and slicing
# print(array[::3])


# fancy indexing
#printing multiple element of array
# print(array[[0,2,4]])
print(array[array>3])