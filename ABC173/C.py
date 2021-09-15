H, W, K = map(int, input().split())
matrix = [[0] * W for _ in range(H)]
for i in range(H):
    l = input()
    for j in range(W):
        if l[j] == '#':
            matrix[i][j] = 1

cnt = 0
for i in range(H):
    for j in range(W):
        

for e in matrix:
    print(e)
