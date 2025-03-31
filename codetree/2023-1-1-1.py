from collections import deque

N,M,K = map(int, input().split())
board=[list(map(int,input().split())) for _ in range(N)]
attack=[[0]*M for _ in range(N)]

def lazer(sx,sy,ex,ey):
    q = deque()
    q.append((sx,sy))

    visited = deque()
    prev = [[(-1,-1) for _ in range(M)] for _ in range(N)]

    while q:
        x,y = q.popleft()
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx,ny = x+dx,y+dy
            nx,ny = nx%N, ny%M
            if board[nx][ny] > 0 and (nx,ny) not in visited:
                q.append((nx,ny))
                visited.append((nx,ny))
                prev[nx][ny]=(x,y)
    
    if prev[ex][ey] == (-1,-1): return False
    else:
        route = deque()
        x,y = prev[ex][ey]
        route.appendleft((x,y))
        while (x,y) != (sx,sy):
            x,y = prev[x][y]
            route.appendleft((x,y))

        return route

for turn in range(1, K+1):
    # 살아남은 포탑 개수 count
    alives = [board[i][j] for i in range(N) for j in range(M) if board[i][j]>0]
    if len(alives)<2: break

    # 공격자 찾기
    min_v = 5001
    ax,ay = 0,0
    for i in range(N):
        for j in range(M):
            if 0 < board[i][j] < min_v:
                min_v = board[i][j]
                ax,ay = i,j
            elif board[i][j] == min_v:
                if attack[i][j] > attack[ax][ay]:
                    ax,ay = i,j
                elif attack[i][j] == attack[ax][ay]:
                    if i+j > ax+ay:
                        ax,ay = i,j
                    elif i+j == ax+ay:
                        if j > ay: 
                            ax,ay = i,j
    board[ax][ay] += (N+M)
    attack[ax][ay] = turn

    # 피공격자 찾기
    max_v = 0
    adx,ady = 0,0
    for i in range(N):
        for j in range(M):
            if (i,j) == (ax,ay): continue
            if board[i][j] > 0 and board[i][j] > max_v:
                max_v = board[i][j]
                adx,ady = i,j
            elif board[i][j] == max_v:
                if attack[i][j] < attack[adx][ady]:
                    adx,ady = i,j
                if attack[i][j] == attack[adx][ady]:
                    if i+j < adx+ady:
                        adx,ady = i,j
                    elif i+j == adx+ady:
                        if j < ady:
                            adx,ady = i,j
    
    # 레이저 공격 시도
    attacked = lazer(ax,ay,adx,ady)
    if attacked:
        board[adx][ady] -= board[ax][ay]
        for x,y in attacked:
            if (x,y)!=(ax,ay):
                board[x][y] -= board[ax][ay]//2
    else: 
        attacked = deque()
        board[adx][ady]-=board[ax][ay]
        for dx,dy in [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]:
            nx,ny = adx+dx,ady+dy
            nx,ny = nx%N, ny%M
            if (nx,ny)!=(ax,ay):
                board[nx][ny] -= board[ax][ay]//2
                attacked.append((nx,ny))
            
    
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and (i,j)!=(ax,ay) and (i,j)!=(adx,ady) and (i,j) not in attacked:
                board[i][j]+=1

max_v = 0
for line in board:
    max_v = max(max_v, max(line))
print(max_v)
        


