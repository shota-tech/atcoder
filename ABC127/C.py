n, m = map(int, input().split())
max_l = 1
min_r = n 

for _ in range(m):
    l, r = map(int, input().split())
    max_l = max(max_l, l)
    min_r = min(min_r, r)

ans = max(min_r - max_l + 1, 0)
print(ans)