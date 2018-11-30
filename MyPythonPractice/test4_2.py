sum=j=1
while j<=3:
    f=1
    for i in range(2,2*(j+1)):
        f*=i
    sum+=f
    j+=1
print("sum=",sum)