n = int(input())
d = {}

for i in range(1, n+1):
    s, p = input().split()
    p = int(p)
    d[i] = (s, p)

d = sorted(d.items(), key=lambda x:x[1][1], reverse=True)
d = sorted(d, key=lambda x:x[1][0])

for e in d:
    print(e[0])