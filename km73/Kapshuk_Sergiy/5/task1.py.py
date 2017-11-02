from random import randrange
e = int(input('кількість однокласників='))
a = [randrange(100, 200) for i in range(e)]
for i in range(e-1):
    for j in range(e-i-1):
        if a[j] < a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
print(a)
x = int(input('зріст Петі='))
for i in range(e):
    if a[i]<x:
        print(i+1)
        break
    elif a[e-1] > x:
        print(e+1)
        break
