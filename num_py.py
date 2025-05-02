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
#Broadcasting
# array = np.array([1,2,3,4,5,6])
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


#boolean masking
# print(array[array>3])



#Reshape() array: change the dimension from 1d to 2d or 3d of the array without changing the value of the elements

# print(array.reshape(3,2))



#ravel() : to convert 3d or 2d array into 1d array
#ravel returns a view, (modify the original array)

# arr = np.array([[1,2,3],[3,4,5],[5,6,7]])
# print(arr.ravel())
# arr.ravel()


#it return the copy of the array, does not affect the original array 
# arr.flatten()
# print(arr.flatten())
# print(arr)
# arr


#insert a element in an array
# we cannot directly insert an element since arrays are of fixed size, we have to create new array 
#use insert()
# arr = np.array([1,2,3,4,5])
# new_arr = np.insert(arr, 0,0)
# print(new_arr)

# Insert in 2d array
# arr = np.array([[1,2],[3,4],[5,6]])
# new_arr = np.insert(arr, 0,[0,1], axis = 0)
# print(new_arr)



# append in array
# new_array = np.append(array, [7,8,9])
# print(new_array)

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# new_arr = np.concatenate((arr1,arr2), )
# print(new_arr)


#deleting element
# arr = np.array([1,2,3,4,5])
# new_arr = np.delete(arr, 2)
# print(new_arr)


# arr = np.array([[1,2,3],[3,4,5]])
# new_arr = np.delete(arr, 0, axis = 1)
# print(new_arr)


# Merging 2d arrays
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# print(np.vstack((arr1,arr2))) # for verticlly merging 
# print(np.hstack((arr1,arr2)))# for horizontally mearging or normal mearge
# new_arr = np.vstack((arr1, arr1))
# print(new_arr)



#Split array

# arr = np.array([1,2,3,4,5,6])
# # print(np.split(arr,2))
# new_arr = np.split(arr,1)
# print(new_arr)

#broadcasting
# array = np.array([100,200,300])
# print(array - (array * 10/100 ))

# matrix = np.array([[1,2,3], [4,5,6]])
# arr = np.array([[10,11,12]])
# result = matrix + arr
# print(result)

# Dealing with NaN values


arr = np.array([1,2,3,4,np.nan, 5, np.nan])
# print(np.isnan(arr))
print(np.nan_to_num(arr, nan=5))
print(arr)
array = np.array([1,2,3,4,np.inf, -np.inf])
print(np.isinf(array))