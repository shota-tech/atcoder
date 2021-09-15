n, m = map(int, input().split())
l = []

for _ in range(m):
    s = list(map(int, input().split()))[1:]
    l.append(s)

p = list(map(int, input().split()))
ans = 0

for i in range(2 ** n):
    tmp = [0] * n
    flg = False
    for j in range(n):
        if i >> j & 1:
            tmp[j] = 1
    for i, s in enumerate(l):
        cnt = sum([tmp[e-1] for e in s])
        if cnt % 2 != p[i]:
            flg = True
            break
    if not flg:
        ans += 1

print(ans)

