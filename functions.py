# # function defination
# def calc_sum(a, b):
#     sum = a+b
#     print(sum)


# # function call
# calc_sum(51, 2)

# def cal_sum(x, y):# function defination (parameters)
#     return x + y


# a = int(input("give first value :"))
# b = int(input("give second value :"))
# sum = cal_sum(a, b)#function call (Arguments)
# print("sum = ",sum)


# average of three numbers

# def avg(a, b, c):
#     return (a + b + c)/3

# a = int(input("give first value :"))
# b = int(input("give 2nd value :"))
# c = int(input("give 3rd value :"))
# average = avg(a, b, c)
# print(average)

#Function that returns the maximun value among two numbers

def max(a, b):
    if(a > b ):
        return a
    else:
        return b
    
a = 5
b = 1
print(max(a, b))