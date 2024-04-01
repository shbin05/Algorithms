"""
n: 드래곤 커브 개수
x, y: 드래곤 커브 시작 점 (0 < = x,y <= 100)
d: 시작 방향
g: 세대

방향
0: >
1: ^
2: <
3: v
"""

n = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]

# 동북서남
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


for _ in range(n):
    x, y, d, g = map(int, input().split())
    board[y][x] = 1

    curve = [d]
    for j in range(g): # 커브 리스트 만들기
        for k in range(len(curve)-1, -1, -1):
            curve.append((curve[k]+1)%4)
    
    for j in range(len(curve)): # 드래곤 커브 만들기
        x += dx[curve[j]]
        y += dy[curve[j]]

        if x < 0 or x >= 101 or y < 0 or y >= 101: continue
        board[y][x] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i+1][j]==1 and board[i][j+1] == 1 and board[i+1][j+1] ==1 :
            answer+=1

print(answer)