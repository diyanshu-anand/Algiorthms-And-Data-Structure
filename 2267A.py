t = int(input())

while(t):
  
    line = input().split()
    n = int(line[0])
    c = line[1]
    
    s = input()
    cost = 0 
    
    for i in range(0, n // 2, 1):
   
        if(s[i] == s[n-i-2+ 1]):
           cost += 0
        elif(s[i] != s[n-i-2+1] and (s[i] == c or s[n-i-2+1] == c)):
           cost += 1
        else:
           cost += 2
           
    print(cost)
    
    t -= 1
