a=''
k=0
for i in range(100,1000):
    if i%17==0:
        k+=1
        a+=str(i) + ' '
print(a,k)