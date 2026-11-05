a=float(input())
k=0
while a!=0:
    b=float(input())
    if b==0:
        break
    if b<a:
        k+=1
    a=b
print(k)