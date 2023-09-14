def sum(n1, n2):
    result = n1 + n2
    return result


total = sum(33, 12)
print("total : ", total)


# default Parameter:
def viewCount(option1, option2, option3=5):
    return option1 + option2 + option3


print(viewCount(12, 14))


# Argument :
def all_sum(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum += num
        print("total sum of the tuple : ", sum)


n = all_sum(5, 1, 4, 5)
print(n)


def new_func(*args):
    print(args)


my_Func = new_func(45, "string ", True)
print("function invoke: ",my_Func)
