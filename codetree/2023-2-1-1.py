L, N, Q = map(int, input().split())

board = [[0]*L for _ in range(L)] # 기사들 위치 저장할 배열
spike =[[0]*L for _ in range(L)] # 함정 위치 저장할 배열
wall = [[0]*L for _ in range(L)] # 벽 위치 저장할 배열

for i in range(L):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 1: spike[i][j] = 1
        elif line[j] ==2: wall[i][j] = 1

pos = [() for _ in range(N+1)]
hp = [0]*(N+1)
hw = [() for _ in range(N+1)]
alive = [True]*(N+1)
dmg = [0]*(N+1)

for i in range(1, N+1): 
    r, c, h, w, k = map(int, input().split())
    r, c = r-1, c-1
    pos[i] = (r,c)
    hw[i] = (h,w)
    hp[i] = k

def area(idx):
    square = []
    r, c = pos[idx][0], pos[idx][1]
    h, w = hw[idx][0], hw[idx][1]
    for i in range(r, r+h):
        for j in range(c, c+w):
            if 0 <= i < L and 0 <= j < L:
                square.append((i,j))
    
    return square

def update_board():
    global board

    board = [[0]*L for _ in range(L)]
    for i in range(1, N+1):
        if not alive[i]: continue
        square = area(i)
        for x, y in square:
            board[x][y] = i

def check(idx, d):
    global mv

    square = area(idx)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for x,y in square:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < L and 0 <= ny < L:
            if wall[nx][ny]: 
                mv.clear()
                return
            elif board[nx][ny] != 0 and board[nx][ny] != idx:
                if board[nx][ny] not in mv:
                    mv.append(board[nx][ny])
                    check(board[nx][ny], d)
        else: 
            mv.clear()
            return
    
    return

def move(mv, d):
    global pos 

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in mv:
        x, y = pos[i]
        nx, ny = x+dx[d], y+dy[d]
        pos[i] = (nx,ny)
    
    update_board()

    return

for _ in range(Q):
    update_board()
    idx, d = map(int, input().split())
    if not alive[idx]: continue
    mv = [idx]
    check(idx, d)
    if len(mv) > 0:
        move(mv, d)
        for i in mv:
            if i == idx: continue
            square = area(i)
            s = 0
            for x,y in square:
                if spike[x][y]: s+=1
            hp[i]-=s
            dmg[i]+=s
            if hp[i] <= 0: alive[i] = False

s = 0
for i in range(1, N+1):
    if alive[i]: s+=dmg[i]

print(s)