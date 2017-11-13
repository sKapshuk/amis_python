def power(a,n):
    k=1
    for i in range(1,n+1,1):
        k=a*k
    return k
n=int(input('Степінь='))
a=float(input('Основа='))
print(power(a,n))

