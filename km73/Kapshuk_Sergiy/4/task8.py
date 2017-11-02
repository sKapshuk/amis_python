q=int(input())
w=int(input())
e=int(input())
r=int(input())
if ((q > 0) and (q <= 8)and(e>0)and(e<=8)):
    if ((w > 0) and (w <= 8)and(r>0)and(r<=8)):
        if((e==q)or(e==q-1)or(e==q+1))and((r==w)or(r==w+1)or(r==w-1)):
            print("YES")
        else:
            print("NO")
    else:
        print("Invalid vaiue")
else:
    print("Invalid value")
