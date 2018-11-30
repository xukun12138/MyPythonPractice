import math
a=0
s=0
b=2*math.pi
n=10000  #分成n份
h=(b-a)/n
t=a
f0=(math.cos(t)+4*math.sin(2*t)+5)**(1/2)
for i in range(1,n+1):  #梯形法
    t+=h
    f1 = (math.cos(t) + 4 * math.sin(2 * t) + 5) ** (1 / 2)
    s=s+(f0+f1)*h/2
    f0=f1
print("s=",s)


a2=0
s2=0
b2=2*math.pi
n2=1000  #分成n份
h2=(b2-a2)/n2
t2=a2
ff0=(math.cos(t2)+4*math.sin(2*t2)+5)**(1/2)
for i in range(1,n2+1):  #矩形法
    ff1 = (math.cos(t2) + 4 * math.sin(2 * t2) + 5) ** (1 / 2)
    s2=s2+((ff0+ff1)/2)*h2
    t2 += h2
    ff0 = ff1
print("s2=",s2)