n=int(input())
for i in range(1,n+1):
    k = 0
    for t in range(1, i):
        if i % t == 0:
            k += t
    if k == i:
        print(i)