# Accepted Code 

t = int(input())

while(t):
    
    n,q = map(int,input().split(" "))
    
    a = list(map(int,input().split(" ")))
    
    prefix = [0]*(n+1)
    
    for i in range(1,n+1):
        prefix[i] = prefix[i-1] + a[i-1]
    
    
    
    while(q):
        
        l,r,k = map(int,input().split(" "))
        org_sum = prefix[r]-prefix[l-1]
        new_sum = prefix[-1]  + k*((r-l)+1) - org_sum
        q -= 1
        
        if(new_sum%2 == 0):
            print("NO")
        else:
            print("YES")
    
    t -= 1
  
    

   
    
  


