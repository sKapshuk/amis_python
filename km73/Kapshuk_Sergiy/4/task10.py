q=int(input())
w=int(input())
e=int(input())
r=int(input())
if ((q > 0) and (q <= 8)and(e>0)and(e<=8)):
    if ((w > 0) and (w <= 8)and(r>0)and(r<=8)):
        if ((abs(q - e)) == (abs(r - w))):
            print("YES")
        elif(e == q ):
            print("YAS")
        elif(w==r):
            print("YAS")
        else:
            print("NO")
    else:
        print("Invalid value")
else:
    print("Invalid value")