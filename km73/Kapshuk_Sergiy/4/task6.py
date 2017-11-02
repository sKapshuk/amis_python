q=int(input())
w=int(input())
e=int(input())
r=int(input())
if ((q > 0) and (q <= 8)):
    if ((w > 0) and (w <= 8)):
        if (e == q ):
            if (((e <= 8) and (e >= 1)) and ((r >= 1) or (r <= 8))):
                print("YES")
            else:
                print("NO")
        elif (r == w):
            if(((e<=8)and(e>=1))and((r>=1)or(r<=8))):
                print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
