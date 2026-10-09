t =  int(input())

while(t):
    p = list(map(int,input().split(" ")))

    count = 0
    for i in range(1,len(p),1):
        if p[i] > p[0]:
            count += 1
    print(count)
    
    t -= 1