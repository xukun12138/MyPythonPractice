p=int(input('p='))
w=int(input('w='))
s=int(input('s='))
if s<250:
    d=1
elif 250 <= s < 500:
    d=0.025
elif 500 <= s < 1000:
    d=0.045
elif 1000 <= s < 2000:
    d=0.075
elif 2000 <= s < 2500:
    d=0.09
elif 2500 <= s < 3000:
    d=0.12
else:
    d=0.15
f=p*w*s*(1-d)
print(f)