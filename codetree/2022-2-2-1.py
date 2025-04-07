from collections import deque

N,M = map(int, input().split())

board = []
camp = []
store = [(-1,-1)]
cur = [(-1,-1) for _ in range(M+1)]
arrived = [0 for _ in range(M+1)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1: camp.append((i,j))
    board.append(line)

camp.sort(key=lambda x: (x[0], x[1]))

for _ in range(M):
    x,y = map(int, input().split())
    store.append((x-1,y-1))

def bfs(sx,sy,ex,ey,type):
    q = deque()
    q.append((sx,sy))

    visited = deque()
    visited.append((sx,sy))

    prev = [[(-1,-1) for _ in range(N)] for _ in range(N)]

    while q:
        x,y = q.popleft()
        if (x,y) == (ex,ey):
            break
        for dx,dy in [(-1,0),(0,-1),(0,1),(1,0)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                if (nx,ny) not in visited and board[nx][ny]!=-1:
                    q.append((nx,ny))
                    visited.append((nx,ny))
                    prev[nx][ny]=(x,y)

    if type==1:
        if prev[ex][ey] == (-1,-1):
            return 99999
        elif prev[ex][ey] == (sx,sy):
            return 1
        else:
            len = 2
            x,y = prev[ex][ey]
            while prev[x][y] != (sx,sy):
                x,y = prev[x][y]
                len+=1
            return len
    if type==2:
        if prev[ex][ey] == (sx,sy):
            return ex,ey
        else:
            x,y = prev[ex][ey]
            while prev[x][y] != (sx,sy):
                x,y = prev[x][y]

            return x,y

t=1
while True:
    if arrived[1:].count(0) == 0: break
    banned = []
    # 베이스라인 선정
    if t<=M:
        ex,ey = store[t]
        mdist = 99999
        mx,my = -1,-1
        for sx,sy in camp:
            if board[sx][sy]==-1: continue
            
            dist = bfs(sx,sy,ex,ey,1)
            if dist < mdist:
                mdist = dist
                mx,my = sx,sy
            
        cur[t] = (mx,my)
        banned.append((mx,my))
    
    # 사람 이동
    for i in range(1, min(M+1, t+1)):
        if arrived[i] == 1: continue 

        sx,sy = cur[i]
        ex,ey = store[i]
        nx,ny = bfs(sx,sy,ex,ey,2)
        cur[i] = (nx,ny)

        if cur[i] == store[i]: 
            arrived[i] = 1
            banned.append((nx,ny))
    
    for x,y in banned:
        board[x][y] = -1

    t+=1


print(t)