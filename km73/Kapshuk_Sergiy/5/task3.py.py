from random import randrange
e = int(input('кількість чисел='))
a = [randrange(0, 10) for i in range(e)]
print(a)
list = []
for i in range(e):
    noequal = 0
    for j in range(e):
        if (a[j] == a[i]):
            noequal = noequal + 1
    if noequal == 1:
        list.append(a[i])
print(list)