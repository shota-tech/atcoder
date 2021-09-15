N = int(input())
a = N % 1000
ans = 0 if a == 0 else 1000 - a
print(ans)