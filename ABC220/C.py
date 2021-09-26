import sys

n = int(input())
a = list(map(int, input().split()))
x = int(input())

sum_a = sum(a)
q, mod = divmod(x, sum_a)

k = len(a) * q
num = 0
for i in range(10 ** 100 - q):
    for e in a:
        k += 1
        num += e
        if num > mod:
            print(k)
            sys.exit()
