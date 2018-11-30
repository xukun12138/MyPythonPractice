x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
s=x**2+y**2+z**2
if s>1000:
    print(s//10000)
else:
    print(x+y+z)