def minimum(list):
    if len(list)==0:
        return
    if len(list)==1:
        return list[0]
    min=minimum(list[1:])
    x = (min if min < list[0] else list[0])
    print(x)
    return x


list=[2, -6, -1, 0, -2]
print(minimum(list))