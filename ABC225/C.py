import sys
n, m = map(int, input().split())
a = '0123456'
l2 = []
before = 0
for i in range(n):
    b = list(map(int, input().split()))
    if i != 0 and b[0] != before + 7:
        print('No')
        sys.exit()
    before = b[0]
    l = [divmod(e-1, 7) for e in b]
    if len(set([e[0] for e in l])) != 1:
        print('No')
        sys.exit()
    s = ''.join([str(e[1]) for e in l])
    if s not in a:
        print('No')
        sys.exit()
    l2.append(s)
print('Yes' if len(set(l2)) == 1 else 'No')