import math

from functools import reduce
K = int(input())
sum = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            nums = [a, b, c]
            gcd = reduce(math.gcd, nums)
            sum += gcd
print(sum)