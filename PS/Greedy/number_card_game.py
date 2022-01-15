n, m = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

mins = []
for i in arr:
        mins.append(min(i))

print(max(mins))