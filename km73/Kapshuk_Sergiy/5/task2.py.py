from random import randrange
e = int(input('кількість чисел='))
a = [randrange(0, 10) for i in range(e)]
print(a)
count = 0
for i in range(e):
    for j in range(e):
        if (a[j] == a[i]) and (i != j):
         count = count + 1
print(int(count/2))