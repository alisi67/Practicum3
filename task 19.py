n = int(input())
k=2
znam=1
chis=1
for i in range(1,n+k+1):
    chis*=i
for i in range(1,n):
    znam*=i
print(chis//(znam*2))