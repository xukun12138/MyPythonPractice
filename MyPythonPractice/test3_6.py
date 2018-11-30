x=int(input("x="))
y=int(input("y="))
z=int(input("z="))

if (x+y>z and x+z>y and y+z>x) or (x-y<z and x-z<y and y-z<x):
    if x==y==z:
        print('等边三角形')
    elif x==y or x==z or y==z:
        print('等腰三角形')
    elif x**2+y**2==z**2 or x**2+z**2==y**2 or y**2+z**2==x**2:
        print('直角三角形')
    else:
        print('普通三角形')
else:
    print('不能组成三角形')