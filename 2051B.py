t = int(input())



while(t):
    
    n,a,b,c = map(int,input().split(" "))

    s = a+b+c
 
    v = n//s

    w = v*s

    d = v*3

    count = 0
    
    if n == w:
        count = 0
    elif n<=a+w:
        count += 1
    elif n<= a+b+w:
        count += 2
    else:
        count += 3
    
    print(count+d)
    
    t -= 1




    
        
    
    



