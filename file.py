#read mode i.e "r"

# f = open("text.txt", "r")
# data = f.read()
# # print(data)
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)


# write mode i.e "w"(overwrite) and "a"(append)
# f = open("text.txt", "w")
# f.write("hi i am mehdi")
# f =  open("text.txt", "a")
# f.write("\nand i am ali")
# f.close()


# if any txt file does not exixt in our folder then these mode automically create a file

f = open("sample.txt", "a")

# "r+" mode read and overwrite(pointer start) -> no truncate
#  "w+" mode read and overwrite(poinetr start) -> truncate
#  "a+" mode read and overwrite (pointer end) -> no truncate

# with open("text.txt", "r") as f:
#     data = f.read()
#     print(data)
# with automatically close the file
    
# with open("text.txt", "w") as f:
#     f.write("hi")
import os

os.remove("text.txt")

    