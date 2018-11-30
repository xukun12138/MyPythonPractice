import math
a=float(input("输入正的实数："))
myinteger=int(a)
mydecimals=a-myinteger

print("整数部分："+str(myinteger)+"\n小数部分："+str(mydecimals))

print(a)
print(math.modf(a))
