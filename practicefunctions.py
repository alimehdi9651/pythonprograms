nums = [1, 2, 3, 4, 5, 6]
def print_len(abc):
    print(len(abc))

# print_len(nums)
def print_list(list):
    for i in list:
       print(i, end=" ")

# print_list(nums)

def factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact *= i
    return fact
    
# n = 6
# fac = factorial(n)
# print(fac)

# def inr(a):
#     amt = 83.39 * a
#     return amt

# n = float(input("enter amount in $:"))
# d = inr(n)
# print(n," USD =",d,"INR")


def check(a):
    if(a % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

n = 8
check(n)