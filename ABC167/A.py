s = input()
t = input()

if t[:-1] == s and len(t) == len(s) + 1:
    print('Yes')
else:
    print('No')