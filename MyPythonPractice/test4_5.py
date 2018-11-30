sum1=0
for n1 in range(1,1001):
    sum1+=(1/(4*n1-3))-(1/(4*n1-1))
print(4*sum1)

sum2=0
n2=1
var=1
while var==1:
    sum2+=(1/(4*n2-3))-(1/(4*n2-1))
    n2+=1
    if abs(-1/(4*n2-1))<10**(-6):break
print(4*sum2)