print("Enter coordinate of first square")
x0=int(input())
y0=int(input())
print("Enter coordinate of second square")
x1=int(input())
y1=int(input())
if (1<=x0<=8) and (1<=y0<=8) and (1<=x1<=8) and (1<=y1<=8):
    x2=x0-x1
    y2=y0-y1
    if (x2==y2) or (x2==-y2) or (x0==x1) or (y0==y1):
        answer="YES"
    else:
        answer="NO"
else:
    answer="YOU ARE AN IDIOT"
print(answer)
