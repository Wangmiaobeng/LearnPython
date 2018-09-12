from math import sqrt
# 2-100里面的素数
j=2
    i=2
    while i<=k:
        if j%i==0:
            break
        else:
            i=i+1
    if i>k:
        print(j)
    j+=1


