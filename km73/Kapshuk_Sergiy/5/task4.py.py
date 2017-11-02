n = int(input('кількість кеглів='))
k = int(input('скільки кинуто шарів? '))
a = []
f=['.']
for i in range(n):
    a.append(i+1)
for i in range(k):
    print('k[',i+1,']=')
    li = int(input('від '))
    ri = int(input('до '))
    d = ri - li +1
    a[li-1:ri] = f * d
for i in range(n):
    if a[i] != '.':
        a[i] = '|'
print(a)