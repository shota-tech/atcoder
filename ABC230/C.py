n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

if a < b:
    c = 1
    d = b - a + 1
elif a > b:
    c = a - b + 1
    d = 1
else:
    c = 1
    d = 1

if a + b < n + 1:
    e = 1
    f = a + b - 1
elif a + b > n + 1:
    e = a + b - n
    f = n
else:
    e = 1
    f = n


for i in range(p, q + 1):
    l = ""
    for j in range(r, s + 1):
        if j == d + p - c:
            l += "#"
        elif j == f - p + e:
            l += "#"
        else:
            l += "."
    d += 1
    f -= 1
    print(l)
