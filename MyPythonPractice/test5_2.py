n=1
s=0
while s<8.0:
    s+=(1.0/n)
    n+=1
    a=abs(s-8.0)
    print(a,n-1,s)