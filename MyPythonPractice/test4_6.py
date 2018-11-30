a,b=2,1
sum=0
for i in range(3):
    sum+=a/b
    a,b=a+b,a
print(sum)