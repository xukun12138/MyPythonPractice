sum=0
max=0
for i in range(1,101):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count%2==1:
        sum+=1
        print(i)
        if max<i:
            max=i
print(max)