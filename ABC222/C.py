def janken(p1, p2):
    if p1 == p2:
        return 0, 0
    elif p1 == 'G' and p2 == 'C':
        return 1, 0
    elif p1 == 'C' and p2 == 'P':
        return 1, 0
    elif p1 == 'P' and p2 == 'G':
        return 1, 0
    else:
        return 0, 1


n, m = map(int, input().split())
l1 = []

for _ in range(n*2):
    a = list(input())
    l1.append(a)

l2 = [[i, 0] for i in range(n*2)]
for i in range(m):
    for k in range(n):
        p1 = l1[l2[2*k][0]][i]
        p2 = l1[l2[2*k+1][0]][i]
        result = janken(p1, p2)
        l2[2*k][1] += result[0]
        l2[2*k+1][1] += result[1]
    
    l2 = sorted(l2, key=lambda x: (x[1], -x[0]), reverse=True)

for e in l2:
    print(e[0]+1)