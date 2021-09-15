s = list(input())
t = list(input())
ans = 0
for i, e in enumerate(s):
    if e != t[i]:
        ans += 1
print(ans)