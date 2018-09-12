from math import sqrt
# 2-100里面的素数
j=1
while j<=100:
    i=2
    k=sqrt(j)
    while i<=k:
        if j%i==0:
            break
        else:
            i=i+1
    if i>k:
        print(j)
    j+=1


