# dictionary are mutable ,unordered and do not allow duplicate keys
# info = {
#     "college name" : "AIMT",
#     "name" : "ali",
#     "age" : 22
# }
# # print(info)
# # print(info["college name"])
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
print(info1["subjects"]["bio"])