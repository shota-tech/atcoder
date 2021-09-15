X, N = map(int, input().split())
l = list(map(int, input().split()))
min_abs = 51
ans = 0
for i in range(102):
    if i in l:
        continue
    if abs(i - X) < min_abs:
        min_abs = abs(i - X)
        ans = i
print(ans)