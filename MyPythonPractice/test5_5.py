count=0
for i in range(1,100):
    for j in range(1, 100):
        if i>j:
            for k in range(1, 100):
                if j>k:
                    if (i**2)*(j**2)==((i**2)+(j**2))*k**2 and i+j+k<100:
                        count+=1
print(count)