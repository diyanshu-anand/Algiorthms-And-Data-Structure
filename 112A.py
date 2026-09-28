
# Accepted Code

s1 = input()
s2 = input()

count = 0
for i in range(len(s1)):
    
    
    if ord(s1[i].lower())<ord(s2[i].lower()):
        print(-1)
        break
    elif ord(s2[i].lower())<ord(s1[i].lower()):
        print(1)
        break
    
    if ord(s1[i].lower()) == ord(s2[i].lower()):
        count += 1
       
    
# for i in range(len(s1)):
#     print(ord(s1[i].lower()))

# print(count)
# print(count)
if (count == len(s1)):
    print(0)
