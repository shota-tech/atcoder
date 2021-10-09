n, p = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0

for a in l:
    if a < p:
        cnt += 1

print(cnt)