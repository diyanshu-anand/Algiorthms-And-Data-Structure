t = int(input())

while(t):
    
    
    n = int(input())
    a = list(map(int,input().split(" ")))
    # flag = True
    
   
    count0 = a.count(0)
    count1 = a.count(1)
    # print(count0 , count1)
    if(count1 >= count0):
        print("Bessie")
    else:
        print("Elsie")
    #     if flag == True:
    #         c = max(a[i],a[i+1])
    #         a[i+1] = c
    #         flag = False
    #     else:
    #         c = min(a[i],a[i+1])
    #         a[i+1] = c
    #         flag = True

       
    # if len(a)%2 != 0:
    #     if((a[-1] == 0 and a[-2] == 1) or (a[-1] == 1 and a[-2] == 0) or (a[-1] == 1 and a[-2] == 1) ):
    #         print("Bessie")
    #     else:
    #         print("Elsie")
    # else: 
    #     if (a[-1] == 0 and a[-2] == 1) or (a[-1] == 1 and a[-2] == 0) or (a[-1] == 0 and a[-2] == 0):
    #         print("Elsie")
    #     else:
    #         print("Bessie") 
        
  
    t -= 1
    
    
    # if len(a)%2 != 0:
    #     if((a[-1] == 0 or a[-2] == 1) or (a[-1] == 1 or a[-2] == 0) or (a[-1] == 1 and a[-2] == 1) ):
    #         print("Bessie")
    #     else:
    #         print("Elsie")
    # else: 
    #     if (a[-1] == 0 or a[-2] == 1) or (a[-1] == 1 or a[-2] == 0) or (a[-1] == 0 and a[-2] == 0):
    #         print("Elsie")
    #     else:
    #         print("Bessie")