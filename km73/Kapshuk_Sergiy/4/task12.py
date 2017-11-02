n=int(input())
m=int(input())
k=int(input())
if (n>0)and(m>0)and(k>0):
    if (n*m>k):
        if (k%m==0)or(k%n==0):
         print("YES")
        else:
         print("NO")
    else:
     print("NO")
else:
 print("Invalid value")