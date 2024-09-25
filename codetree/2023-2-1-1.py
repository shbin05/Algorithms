from collections import deque

L, N, Q = map(int, input().split())

board = [[0]*L for _ in range(L)] # 기사들 위치 저장할 배열
others = [[0]*L for _ in range(L)] # 벽 위치 저장할 배열

for i in range(L):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 1: others[i][j] = 1
        elif line[j] ==2: others[i][j] = 2

pos = [() for _ in range(N+1)] # 기사 위치 저장
hp = [0]*(N+1) # 기사 체력 저장
hw = [() for _ in range(N+1)] # 기사 범위 저장
alive = [True]*(N+1) # 기사 생존여부 저장
dmg = [0]*(N+1) # 기사 피해량 저장

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
    q = deque()
    q.append(idx)

    mv = set([])
    mv.add(idx)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    flag = True

    while q and flag:
        cur = q.popleft()
        square = area(cur)
        for x,y in square:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < L and 0 <= ny < L:
                if others[nx][ny] == 2: 
                    mv.clear()
                    flag = False
                    break
                elif board[nx][ny] != 0 and board[nx][ny] != cur:
                    q.append(board[nx][ny])
                    mv.add(board[nx][ny])
            else:
                mv.clear()
                flag = False
                break
    
    return mv

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
    mv = check(idx, d)
    if len(mv) > 0:
        move(mv, d)
        for i in mv:
            if i == idx: continue
            square = area(i)
            s = 0
            for x,y in square:
                if others[x][y] ==1: s+=1
            hp[i]-=s
            dmg[i]+=s
            if hp[i] <= 0: alive[i] = False

s = 0
for i in range(1, N+1):
    if alive[i]: s+=dmg[i]

print(s)