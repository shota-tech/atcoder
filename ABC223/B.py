s = list(input())
l = []
for _ in range(len(s)):
    e = s.pop(0)
    s.append(e)
    l.append(''.join(s))
l = sorted(l)
print(l[0])
print(l[-1])