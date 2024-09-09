from collections import deque

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
score = 0
num = 1

def check(x,y,d):
    if d == 'down':
        if x + 2 < R+3:
            if board[x+2][y] == 0 and board[x+1][y-1] == 0 and board[x+1][y+1] == 0: 
                return True
            else: 
                return False
    elif d == 'left':
        if y - 2 >= 0:
            if board[x][y-2] == 0 and board[x-1][y-1] == 0 and board[x+1][y-1] == 0:
                return True
            else:
                return False
    elif d == 'right':
        if y + 2 < C:
            if board[x][y+2] == 0 and board[x-1][y+1] == 0 and board[x+1][y+1] == 0:
                return True
            else:
                return False
    
    return False

def move(x, y, d):
    while True:
        if check(x, y, 'down'): 
            x += 1
        elif check(x, y, 'left') and check(x, y-1, 'down'): 
            y -= 1
            x += 1
            d -= 1
            d %= 4
        elif check(x, y, 'right') and check(x, y+1, 'down'):
            y += 1
            x += 1
            d += 1
            d %= 4
        else: 
            break

    return x, y, d

def clear():
    global board
    board = [[0]*C for _ in range(R+3)]
    return

def bfs(x,y):
    max_value = 0
    
    q = deque()
    q.append((x,y))

    visited = deque()
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R+3 and 0 <= ny < C and (nx,ny) not in visited and board[nx][ny] != 0:
                if board[x][y] == board[nx][ny] or board[nx][ny] == -board[x][y] or board[x][y] < 0:
                    # 골렘 내 이동, 골렘의 출구로 이동, 현재 출구인 경우
                    q.append((nx,ny))
                    visited.append((nx,ny))
                    max_value = max(nx, max_value)
    
    #print(max_value-2)
    return max_value-2

for (c,d) in start:
    # c : 열 번호
    # d : 출구 방향
    x,y = 1,c # 처음 골렘 중앙 위치
    x, y, d = move(x,y,d)
    if x < 4: clear()
    else: 
        board[x][y] = num
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if i == d: board[nx][ny] = -num
            else: board[nx][ny] = num
        score += bfs(x,y)
    num+=1
    
    """for line in board:
        print(line)
    print()"""

print(score)