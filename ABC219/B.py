s1 = input()
s2 = input()
s3 = input()
t = input()

l = [s1, s2, s3]
ans = ''
for e in t:
    ans += l[int(e)-1]

print(ans)