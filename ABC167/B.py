a, b, c, k = map(int, input().split())

if k <= a:
    sum = k
elif k <= a + b:
    sum = a
else:
    sum = a - (k - a - b)

print(sum)
