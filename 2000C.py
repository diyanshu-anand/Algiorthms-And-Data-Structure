s = input()

a = list(map(int,input().split(" ")))

freq = {}

for i in range(len(a)):
    if a[i] == s[i]:
        freq[a[i]] += 1
    else:
        freq[a[i]] = 1

print(freq)



    