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
identity_matrix = np.eye(5)
print(identity_matrix)