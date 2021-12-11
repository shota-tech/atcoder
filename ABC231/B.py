n = int(input())
d = {}
for _ in range(n):
    s = input()
    if d.get(s):
        d[s] += 1
    else:
        d[s] = 1
print(max(d, key=d.get))
