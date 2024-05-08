# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# factorial of a number n
fact = 1
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    print("END")
    return factorial(n-1) * n
    
print(factorial(1))