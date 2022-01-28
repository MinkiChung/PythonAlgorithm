n = int(input())
ls = list(map(int, input().split()))
ls.sort()
sum = 0

for i in ls:
    for j in range(ls.index(i)):
        sum += ls[j]

print(sum)