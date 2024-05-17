# ABSTRACTION -> Hiding the implementation details of the class
# #  and only showing thefeatures to the user
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.clutch = False
#         self.brk = False

#     def start_car(self):
#         self.acc = True
#         self.brk = True
#         print("car started..")

# car1 = Car()
# car1.start_car()


# ENCAPSULATION-> wrapping data and function into a single unit (object)
#everything which we studied till now is an example of encapsulation 


#Create account class with 2 attri balance and account number
#and WAF that debit and credit ammount                                          
# class Account:
#     def __init__(self, blnc, acc_no):
#         self.balance = blnc
#         self.account_no = acc_no

#     def debit(self,amt):
#         self.balance -= amt
#         print("Rs.", amt ,"is debited")
#         print("total balance = ", self.balance)
#     def credit(self,amt):
#         self.balance += amt
#         print("Rs.", amt, "is credited")
#         print("total balance =", self.balance)

#     def print_baalance(self):
#         return self.balance
    

# acc1 = Account(10000, 12345)
# acc1.debit(200)

# acc1.credit(500)
# acc1.credit(50000)
# acc1.debit(45000)
# print("Yout current balance =",acc1.print_baalance())



# del keyword -> which is use to delete any object or attribute of an object
# private attribute -> to make any attribite private we have to simply apply two 
# underscore before the name of any attribute
# class Student:
#     def __init__(self, name, password):
#         self.name = name
#         self.__password = password #here __password is a private attribute of student class.
# #this private attribute only lies in class
#     def print_pass(self):
#         print(self.__password)
# s1 = Student("ali","manali24")

# # del s1.name  
# print(s1)
# s1.print_pass()
# print(s1.__password)

# INHERITANCE -> when one class drives the properties(attributes) and method of another class.

class Car():
    colour = "black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("Car stoped")

# Inheritance are to three types:
#1 Single level inheritance
#2 multi level inheritance 
#3 Multiple inheritance
    
class ToyotaCars(Car):  # this is a example of single inheritance

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print (self.name)
class KIA():
    def __init__(self, type):
        self.type = type

class Fortuner(ToyotaCars):# this is the example of multi inheritance.

    def __init__(self, type):
        self.type = type

car1 = Fortuner("prtrol")
print(car1.type)
# car1.start()

class Saltos(Car , KIA): # this is example of multiple inheritance
    def __init__(self, type):
        self.type = type

car2 = Saltos("Eletric")
print(car2.type)
car2.start()
