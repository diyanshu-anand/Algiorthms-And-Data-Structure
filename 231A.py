n = int(input())

count = 0

while(n):
    a = list(map(int,input().split(" ")))
    if(a.count(1)>1):
        count += 1
    n -=1 
    
print(count)