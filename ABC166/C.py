n, m = map(int, input().split())
h = list(map(int, input().split()))
h2 = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    h2[a-1] = max(h2[a-1], h[b-1])
    h2[b-1] = max(h2[b-1], h[a-1])

ans = 0
for i in range(n):
    if h[i] > h2[i]:
        ans += 1

print(ans)