from collections import deque

L,N,Q = map(int, input().split())
board = []
traps = deque()
for i in range(L):
    line = list(map(int,input().split()))
    for j in range(L):
        if line[j] == 2: 
            line[j]=-1
        elif line[j] == 1: 
            line[j] = 0 
            traps.append((i,j))
    board.append(line)

knights=[(0,0)]
squares=[(0,0)]
hp=[0]
dmg=[0]*(N+1)
for i in range(1,N+1):
    r,c,h,w,k = map(int, input().split())
    knights.append((r-1,c-1))
    squares.append((h,w))
    hp.append(k)

def in_board(x,y):
    if 0<=x<L and 0<=y<L: return True
    else: return False

def init():
    for idx in range(1, len(knights)):
        if hp[idx]>0:
            cx,cy = knights[idx]
            h,w = squares[idx]
            for i in range(cx,cx+h):
                for j in range(cy,cy+w):
                    board[i][j] = idx
        else:
            cx,cy = knights[idx]
            h,w = squares[idx]
            for i in range(cx,cx+h):
                for j in range(cy,cy+w):
                    board[i][j] = 0

def can_move(idx,d):
    dlist = [(-1,0),(0,1),(1,0),(0,-1)]
    dx,dy = dlist[d]

    q = deque()
    q.append(idx)

    moved = set()
    moved.add(idx)

    while q:
        ci = q.popleft()
        cx,cy = knights[ci]
        h,w = squares[ci]
        for x in range(cx,cx+h):
            for y in range(cy,cy+w):
                nx,ny = x+dx, y+dy
                if not in_board(nx,ny) or board[nx][ny] == -1: return False
                elif board[nx][ny] > 0 and board[nx][ny]!=ci and board[nx][ny] not in moved: 
                    q.append(board[nx][ny])
                    moved.add(board[nx][ny])
    return moved

def move(moved, d):
    dlist = [(-1,0),(0,1),(1,0),(0,-1)]
    dx,dy = dlist[d]

    for idx in moved:
        cx,cy = knights[idx]
        h,w = squares[idx]
        for x in range(cx,cx+h):
            for y in range(cy,cy+w):
                board[x][y] = 0
        nx,ny = cx+dx, cy+dy
        knights[idx] = (nx,ny)

    for idx in moved:
        cx,cy = knights[idx]
        h,w = squares[idx]
        for x in range(cx,cx+h):
            for y in range(cy,cy+w):
                board[x][y] = idx

def count_dmg(idx):
    cnt = 0
    for x,y in traps:
        if board[x][y] == idx:
            cnt+=1
    hp[idx]-=cnt
    dmg[idx]+=cnt
    
    return

for _ in range(Q):
    init()
    i,d = map(int, input().split())
    if hp[i] < 1: continue
    moved = can_move(i,d)
    if moved: 
        move(moved,d)
        moved.remove(i)
        for idx in moved:
            count_dmg(idx)

dmgs = 0
for i in range(1,len(hp)):
    if hp[i]>0:
        dmgs+=dmg[i]

print(dmgs)