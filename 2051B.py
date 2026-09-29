# t = int(input())

n,a,b,c = map(int,input().split(" "))


s = a+b+c
 
v = n//s

w = v*s

d = v*3

count = 0

while(True):
    if n == w:
        count = 0
    elif n<=a+w:
        count += 1
    elif n<= a+b+w:
        count += 2
    else:
        count += 3
    break

print(count+d)

    
        
    
    



