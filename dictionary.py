# dictionary are mutable ,unordered and do not allow duplicate keys
# info = {
#     "college name" : "AIMT",
#     "name" : "ali",
#     "age" : 22
# }
# # print(info)

# info["name"] = "Mehdi"
# info["is_adult"] = True
# print(info)
# print(info["age"])

# # nested dict

info1 = {
    "name" : "haider",
    "subjects" : {
        "chem" : 72,
        "Phy" : 62,
        "bio" : 78,
    }
}

# print(info1["subjects"]["bio"])


# # basic methods in dictionary
# # .keys()
# print(list(info1.keys()))


# # .values()
# print(list(info1.values()))

# # .items()
# pairs = list(info1.items())
# print(pairs[1])


# .get()
# print(info1["name1"])/ this direct way of retreving data will show error if we accidently 
# or mistakely pass any key vale whic s not present in the dictionary.


# better way of extracting data for a dictionary(if name does not presrnt 
# is the dictionary then .get() will give none (insted of error))
# print(info1.get("name1"))



# .update()
# info1.update({"name1" : "Ali"})
info1["name3"] = "rizvi"
print(info1)