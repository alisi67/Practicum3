n,k,r=map(int,input().split())
c=0
while n<r:
    c+=1
    n+=n*k/100
print(c)