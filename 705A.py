n = int(input())


res = []
for i in range(n):
    if(i%2 == 0):
        res.append("I hate ")
    else:
        res.append("I love ")
    if i != n-1:
        res.append("that")
        
res.append("it")
s = " ".join(res)

print(s)


