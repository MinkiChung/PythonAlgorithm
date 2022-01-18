n, k = map(int, input().split())
ls = []
for i in range(n):
    ls.append(int(input()))

cnt = 0
for i in ls[::-1]:
    if k >= i :
        cnt += (k // i)
        k %= i
    elif k == 0:
        break


print(cnt)