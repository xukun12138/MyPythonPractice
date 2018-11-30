N=int(input("input:"))
Z=0
for i in range(1,N+1):
    if i%2==0:
        Z+=(i/2)-(i**6)
    else:
        Z+=i-i**4
print(Z)