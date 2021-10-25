import itertools

n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for v in itertools.combinations(l, 3):
    a, b, c = v
    if (b[0]-a[0]) * (c[1]-a[1]) != (b[1]-a[1]) * (c[0]-a[0]):
        ans += 1
print(ans)