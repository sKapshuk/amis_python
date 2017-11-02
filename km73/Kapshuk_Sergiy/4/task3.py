q=int(input())
w=int(input())
e=int(input())
if (q<w)and(q<e):
    print(q)
elif(q<w)and(q==e):
    print(e)
elif(q==w)and(q<e):
    print(w)
elif (w<q)and(w<e):
    print(w)
elif(w==e)and(w<q):
    print(w)
else:
    print(e)