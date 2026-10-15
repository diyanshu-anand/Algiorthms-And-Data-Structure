a = [1,2,4,5,6]

ans = list(1 for x in a if x >= 2)

print(sum(ans))