n = int(input())
x, y = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')
for i in range(2 ** n):
    x_ = 0
    y_ = 0
    cnt = 0
    for j in range(n):
        if (i >> j) & 1:
            x_ += l[j][0]
            y_ += l[j][1]
            cnt += 1
    if x_ >= x and y_ >= y:
        ans = min(ans, cnt)
        break

if ans == float('inf'):
    print(-1)
else:
    print(ans)
