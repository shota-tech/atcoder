N, K = map(int, input().split())
l = [False] * N

for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for i in A:
        l[i-1] = True 

print(sum(1 for e in l if not e))

