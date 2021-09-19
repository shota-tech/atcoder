x = input()
d = {}
for i, s in enumerate(x):
    d[s] = i + 1
n = int(input())

points = {}
for _ in range(n):
    s = input()
    point = 0
    for i, e in enumerate(s):
        point += d[e] * 27 ** (10 - i)
    points[s] = point

ans = sorted(points.items(), key=lambda x: x[1])

for s in ans:
    print(s[0])