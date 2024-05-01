# i = 1
# while(i<=100):
#     print(i)
#     i+=1


# while(i>=1):
#     print(i)
#     i-=1


# n = int(input("enter number :"))
# i = 1
# while(i<=10):
#     print(n*i)
#     i+=1


# list = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(list):
#     print(list[i])
#     i+=1

num = (1,2,3,4,5,6,7,8,9)
n = 100
i= 0
c = -1
while i < len(num):
    if(num[i]==n):
        print("number is present at index ",i)
        c+=1
    else:
        print("finding...")
    i+=1
if(c == -1):
    print("number is not present")
