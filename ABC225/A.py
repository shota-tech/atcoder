import itertools
s = list(input())
ans = len(set(list(itertools.permutations(s))))
print(ans)