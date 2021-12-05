import math

n = int(input())
ans = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        continue

    cnt = 0
    for j in range(1, math.floor(math.sqrt(i) + 1)):
        if i % j == 0:
            cnt += 2

    if cnt == 8:
        ans += 1

print(ans)
