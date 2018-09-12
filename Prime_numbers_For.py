from math import sqrt
for j in range(2,101):
    k=int(sqrt(j))
    flag=1
    for i in range(2,k+1):
        if j%i==0:
            flag=0
    if flag:
        print(j)
