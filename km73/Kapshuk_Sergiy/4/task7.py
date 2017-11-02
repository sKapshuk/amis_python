q=int(input())
w=int(input())
e=int(input())
r=int(input())
if ((q > 0) and (q <= 8)and(e>0)and(e<=8)):
    if ((w > 0) and (w <= 8)and(r>0)and(r<=8)):
        if((w%2==0)and(q%2==0))or((w%2==1)and(q%2==1)):
            if((e%2==0)and(r%2==0))or((e%2==1)and(r%2==1)):
                print("YES")
        elif ((w%2==0)and(q%2==1))or((w%2==1)and(q%2==0)):
            if((e%2==0)and(r%2==1))or((e%2==1)and(r%2==0)):
                print("YES")
            else:
                print("NO")
    else:
        print("Invalid value")
else:
    print("Invalid value")