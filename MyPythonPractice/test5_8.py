import math
a=int(input(">"))
x0=a
d=1
while math.fabs(d)>10**(-5):
    x1=x0
    d=(x1**3-a)/(3*x1**2)
    x0=x1-d
print(x0)