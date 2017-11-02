x = []
y = []
countn = 0
county = 0
for i in range(8):
    x.append(int(input('x = ')))
    y.append(int(input('y = ')))
for i in range(8):
    for j in range(8):
        if(((abs(x[i] - x[j])) == (abs(y[i] - y[j]))) or (x[i] == x[j]) or (y[i] == y[j])) and (i != j):
            county = county + 1
        else:
            countn = countn + 1
if (countn > 0)and(county == 0):
    print("NO")
else:
    print("YES")




