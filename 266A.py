n = int(input())
s = input()
p1 = 0
p2 = 1
count = 0

while(p2<len(s)):
    if(s[p1] == s[p2]):
        count += 1
    p1 += 1
    p2 += 1

print(count)
