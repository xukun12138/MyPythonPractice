for i in range(100,1000):
    x=i//100
    z=i%10
    y=(i-x*100-z)//10
    if i//9==x**2+y**2+z**2:
        print(i)