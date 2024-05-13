# syntax of class
# class Student:
#     name = "ali"
#     age = 12
#     height = 5.5
# syntax of instace or object of a class
# S1 = Student()
# print(S1.height)

# Constructor in Object oriented or "__init__() function"


# class Cars():
#     Categorie = "CAR"  #Class attribite

#     def __init__(self, name, brand, model_no):
#         self.name = name  #object atribute
#         self.brand = brand #object atribute
#         self.model_no = model_no #object atribute
#         print("adding new data to the data base")

#object attri have higher precedence than class attribute
#boj att >> class attr

# a1 = Cars("BMW 144d", "BMW", "1298749832")
# print(a1.name,a1.brand)

# car1 = Cars("Saltos", "KIA","001236")
# # print("Model number of", car1.name , "is" ,car1.model_no)    
# print(car1.Categorie)




# # methods in OOPs
# class Student:
#     def __init__(self , name , marks):
#         self.name = name
#         self.marks = marks
    
#     def hello(self):  #mehod in oops
#         print("welcome ", self.name)

#     def print_marks(self):  # method is oops
#         return self.marks


# s1 = Student("Ali", 71)
# # print(s1.marks)
# s1.hello()
# print(s1.print_marks())



# Student clss that take marks and names of three student and WAF that return the average
# class Student:
#     name = "Ali Mehdi"
#     def __init__(self, sub_name, marks):
#         self.sub_name = sub_name
#         self.marks = marks
#     def avg(self):
#         return (sub1.marks + sub2.marks + sub3.marks)/3
    
# sub1 = Student("Physics", 57)
# sub2 = Student("Chemistry", 56)
# sub3 = Student("Biology", 51)

# print(sub1.avg())


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        return sum / 3


s1 = Student("Ali Mehdi", [51,57,54])
print(s1.avg())

