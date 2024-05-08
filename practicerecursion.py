# print sum of first n numbers.

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

# print(sum(4))


# print elements of a list
num = [1, 2, 3, 4, 5]
def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    return print_list(list,idx + 1)

print_list(num)