max1=min1=0
for i in range(1,6):
    sum=0
    for j in range(1,7):
        x=int(input("->"))
        sum+=abs(x)
    if sum>max1:max1=sum
    if i==1 or sum<min1:min1=sum
print(max1,min1)