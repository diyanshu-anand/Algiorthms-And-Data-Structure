t = int(input())

while(t):
    n = int(input())
    a = list(map(int,input().split(" ")))
    

    
    count = 0
    for i in range(len(a)):
        if a[i] == 0:
            count += 1
            
    if a[0] == 0 and a[-1] == 0 :
        print(0)
    elif count <= 1:
        print(-1)
    elif a[0] == 0 and a[-1] !=0 and count>=1:
        print(1)
    elif a[0] != 0 and a[-1] == 0 and count >= 1:
        print(1)
    else:
        print(2)
        
    
    

        
    t -= 1
    

    
        
        

    