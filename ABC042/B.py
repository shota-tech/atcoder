N, L = map(int, input().split())
str_list = []
for _ in range(N):
    S = input()
    str_list.append(S)
print(''.join(sorted(str_list)))