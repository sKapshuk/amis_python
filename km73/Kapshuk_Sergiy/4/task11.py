q=int(input())
w=int(input())
e=int(input())
r=int(input())
if ((q > 0) and (q <= 8)):
    if ((w > 0) and (w <= 8)):
        if (((e==q+2)or(e==q-2))and((r==w+1)or(r==w-1))):
            if(((e<=8)and(e>=1))and((r>=1)or(r<=8))):
             print("Yes")
            else:
             print("no")
        elif (((e==q-1)or(e==q+1))and((r==w+2)or(r==w-2))):
            if (((r <= 8) and (r >= 1)) and ((e >= 1) or (e <= 8))):
             print("Yes")
            else:
             print("No")
        else:
         print("no")
    else:
      print("Invalid value")
else:
 print("Invalid value")