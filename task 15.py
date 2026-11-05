n=int(input())
for i in range(1,n+1):
    k=0
    for t in range(2,i):
        if i%t==0:
            k+=1
            break
    if k==0:
        print(i)