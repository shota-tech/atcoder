n = int(input())
a = list(map(int, input().split()))
q = int(input())

l = [0] * 100001
for i in a:
    l[i] += 1

s = sum(a)

for _ in range(q):
    b, c = map(int, input().split())
    s += (c - b) * l[b]
    l[c] += l[b]
    l[b] = 0
    print(s)
