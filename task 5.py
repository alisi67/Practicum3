a=int(input())
v=''
for i in range(1,a):
    if i**3<a:
        v+=str(i**3) + ' '
print(v)