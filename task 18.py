x=int(input())
yu=0
for i in range(1,int(x**0.5)+1):
    k = 0
    for j in range(2, i):
        if i % j == 0:
            k += 1
            break
    if k == 0:
        for t in range(int(x**0.5),x+1):
            c = 0
            for g in range(2, t):
                if t % g== 0:
                    c += 1
                    break
            if c == 0:
                if t**2 + i**2 ==x:
                    yu += 1
print(yu)

