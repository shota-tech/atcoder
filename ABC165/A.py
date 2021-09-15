K = int(input())
A, B = map(int, input().split())
ans = False

for i in range(A, B+1):
    if i % K == 0:
        ans = True

print('OK' if ans else 'NG')