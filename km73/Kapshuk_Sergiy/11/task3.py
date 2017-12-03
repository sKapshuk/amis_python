def reverse(list):
    if len(list)==1:
        return list
    else:
        return [list[-1]] + reverse(list[:-1])

list=[1, 2, 3, 4, 5, 6, 7, 8]
print(reverse(list))