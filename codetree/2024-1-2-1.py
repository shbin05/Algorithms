R, C, K = map(int, input().split())
start = []
for _ in range(K):
    c, d = map(int, input().split())
    c-=1
    start.append((c,d))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [[0]*C for _ in range(R+3)]

def move(x, y, d):
    while True:
        if board[x+2][y] == 0: x += 1
    
    return

for (c,d) in start:
    # c : 열 번호
    # d : 출구 방향
    x,y = 1,c # 처음 골렘 중앙 위치
    move(x,y,d)