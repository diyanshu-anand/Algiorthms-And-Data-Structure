# Accepted code 

n = int(input())
events = list(map(str,input().strip()))

room = [0]*10

for e in events:
    match e:
        case 'L':
            for i in range(10):
                if room[i] == 0:
                    room[i] = 1
                    break
        case 'R':
            for i in range(9,-1,-1):
                if room[i] == 0:
                    room[i] = 1
                    break
        case num:
            room[int(num)] = 0
            
print("".join(map(str,room)))