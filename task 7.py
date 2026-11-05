a=int(input())
k=0
w=f'{a:b}'
for i in w:
    if i=='0':
        k+=1
if k==len(w)-1:
    print('верно')
else:
    print('неверно')