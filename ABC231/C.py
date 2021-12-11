import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
m = len(a)
for _ in range(q):
    x = int(input())
    print(m - bisect.bisect_left(a, x))
