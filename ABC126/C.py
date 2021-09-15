import math

N, K = map(int, input().split())
sum = 0

for i in range(1, N+1):
    if i >= K:
        sum += 1
        continue

    x = math.ceil(math.log(K/i,2))
    sum += (0.5 ** x)

print(sum / N)