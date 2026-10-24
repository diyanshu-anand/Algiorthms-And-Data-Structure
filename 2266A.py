t = int(input()) 



while(t):
    
    p = int(input())

    a = list(map(int,input().split(" ")))
    
    print(p-min(a))
    
    t -= 1
