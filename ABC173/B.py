N = int(input())

d = {
    'AC': 0,
    'WA': 0,
    'TLE': 0,
    'RE': 0
}

for _ in range(N):
    S = input()
    if S == 'AC':
        d['AC'] += 1
    elif S == 'WA':
        d['WA'] += 1
    elif S == 'TLE':
        d['TLE'] += 1
    else:
        d['RE'] += 1

for k, v in d.items():
    print(k, 'x', v)