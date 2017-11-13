def power(a,n):
    if n==0:
     return 1
    else:
     return (a*power(a,n-1))
n=int(input('Степінь='))
a=float(input('Основа='))
print(power(a,n))