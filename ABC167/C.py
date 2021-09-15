n, m, x = map(int, input().split())
cl = []
al = []

for _ in range(n):
    c, *a = map(int, input().split())
    cl.append(c)
    al.append(a)

ans = float('inf')
for i in range(2 ** n):
    sum = 0
    l = [0] * m

    for j in range(n):
        if i >> j & 1:
            sum += cl[j]
            for k in range(m):
                l[k] += al[j][k]

    flg = all([e >= x for e in l])

    if flg:
        ans = min(ans, sum)

print(-1 if ans == float('inf') else ans)