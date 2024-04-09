h, w, x, y = [int(i) for i in input().split()]
A = [[0 for _ in range(w)] for _ in range(h)]
B = []

for _ in range(h+x):
    B.append([int(i) for i in input().split()])

for i in range(h):
    for j in range(w):
        if i<x or i>=h or j<y or j>=w:
            A[i][j]=B[i][j]
        else:
            A[i][j] = B[i][j]-A[i-x][j-y]

for line in A:
    print(*line)