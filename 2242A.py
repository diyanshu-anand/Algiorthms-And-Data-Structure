t = int(input())

while t:
    k = int(input())
    c = list(map(int, input().split()))

    if any(x >= 3 for x in c):
        print("YES")
    elif sum(1 for x in c if x >= 2) >= 2:
        print("YES")
    else:
        print("NO")

    
    t -= 1
    
    # for i in range(len(c)):
    #     for j in range(i+1,len(c)):
    #         if i == j:
    #             continue
            
    #         a.append([c[i],c[j]])
    #         print(c[i],c[j])
            
            
    
    # if(len(a)-len(set(map(tuple, a)))>0):
    #     print("YES")
    # else:
    #     print("NO")
    # t -= 1