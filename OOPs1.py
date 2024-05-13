# Abstraction -> Hiding the implementation details of the class
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


# Encapsulation -> wrapping data and function into a single unit (object)
#everything which we studied till now is an example of encapsulation 


#Create account class with 2 attri balance and account number
#and WAF that debit and credit ammount                                          
class Account:
    def __init__(self, blnc, acc_no):
        self.balance = blnc
        self.account_no = acc_no

    def debit(self,amt):
        self.balance -= amt
        print("Rs.", amt ,"is debited")
        print("total balance = ", self.balance)
    def credit(self,amt):
        self.balance += amt
        print("Rs.", amt, "is credited")
        print("total balance =", self.balance)

    def print_baalance(self):
        return self.balance
    

acc1 = Account(10000, 12345)
acc1.debit(200)

acc1.credit(500)
acc1.credit(50000)
acc1.debit(45000)
print("Yout current balance =",acc1.print_baalance())