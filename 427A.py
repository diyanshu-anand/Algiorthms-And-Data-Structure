n = int(input()) 


events = list(map(int, input().split()))

p = 0
u = 0

for e in events:
    if e == -1:
        if p > 0:
            p -= 1
        else:
            u += 1
    else:
        p += e

print(u)
