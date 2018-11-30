import math
a = int(input())

# 单分支实现
if a%2==1:
    print(math.sqrt(a))
if a%2==0:
    print(a**(1/3))

# 双分支
if a%2==1:
    print(math.sqrt(a))
else:
    print(a**(1/3))

# 条件
print(math.sqrt(a) if a%2!=0 else a**(1/3))

