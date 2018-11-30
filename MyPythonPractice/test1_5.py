import math

x=12
y=10**(-5)

a=1+(x/(3*2*1))+(y/(5*4*3*2*1))
print(a)                            #(1)

b=(2*math.log(abs(x-y),math.e))/(math.exp(x+y)-math.tan(y))
print(b)                            #(2)

c=((math.sin(x)+math.cos(y))/((x**2)+(y**2)))+((x**y)/(x*y))
print(c)                            #(3)

d=(math.exp(math.pi*x/2))+((math.log10(abs(x-y)))/(x+y))
print(d)