import math
d,x2=1.0,-2.0
while math.fabs(d)>10**(-6):
    x1=x2
    d=((math.exp(-x1))-x1)/(-(math.exp(-x1))-1.0)
    x2=x1-d
print(x2)