n = int(input())
l = []
s = 0

for _ in range(n):
    a, b = map(int, input().split())
    s += a / b
    l.append((a, b))

s /= 2
ans = 0
for t in l:
    a = t[0] / t[1]
    if s > a:
        s -= a
        ans += t[0]
        continue
    else:
        ans += t[1] * s
        break

print(ans)