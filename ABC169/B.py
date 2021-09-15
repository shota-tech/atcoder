import sys
N = int(input())
l = list(map(int, input().split()))
ans = 1

if 0 in l:
    print('0')
    sys.exit()
    
for e in l:
    ans *= e
    if ans > 10 ** 18:
        print('-1')
        sys.exit()

print(str(ans))