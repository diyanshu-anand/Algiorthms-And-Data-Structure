n = int(input())

a = list(map(int,input().split(" ")))

flag = False
for i in range(len(a)):
    if a[i] == 1:
        flag = True
        break
    
if(flag):
    print("HARD")
else:
    print("EASY")
    
    