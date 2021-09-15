N, M = map(int, input().split())
l = list(map(int, input().split()))

sum = 0
for e in l:
    sum += e

x = N - sum
if x < 0:
    print(-1)
else:
    print(x)