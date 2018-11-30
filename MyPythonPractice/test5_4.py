import math
count=0
for n in range(1,22):
    s=2**n-1
    flag=True
    j=int(math.sqrt(s))
    for i in range(2,j+1):
        if s%i==0:
            flag=False
            break
    if flag and s>1:
        count+=1
        print(s)
print(count)