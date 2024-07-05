# Set is the collection of unorderd items.
# each element must be unique and immutable(elements)


# sets = {1, 2, 3, 4 ,4 , "hello", "world", "world", 5}
# # print(type(sets))
# # print(sets)
# sets1 = {}#this not an empty set it is a dictionary i.e empty
# sets2 = set()
# print(sets2)


# basic methods in python

# .add()
collection = {"ali", "mehdi", "is", "a", "good"}
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(2)
# collection.add("hello world")

# print(collection)


# # .remove()

# collection.remove("hello world")
# print(collection)


#.clear() -> it makes the set empty

# collection.clear()
# print(collection)

# .pop() -> it picks a random value throughout the set

# print(collection.pop())
# print(collection)


# .union() and .intersection

st1 = {1,2,3}
st2 = {3,4,5}
print(st1.union(st2))
print(st1.intersection(st2))