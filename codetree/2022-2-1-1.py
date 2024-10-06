N,M,K = map(int, input().split())
g_board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j]!=0: g_board[i][j].append(line[j])

board = [[0]*N for _ in range(N)]
power = [0]*(M+1)
dir = [0]*(M+1)
pos = [() for _ in range(M+1)]
gun = [0]*(M+1)
scores = [0]*(M+1)

for i in range(1,M+1):
    x,y,d,s = map(int, input().split())
    pos[i] = (x-1,y-1)
    board[x-1][y-1] = i
    dir[i] = d
    power[i] = s

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def get_gun(x,y,idx): # 좌표 및 유저idx 입력받음
    global g_board, gun

    if g_board[x][y] and g_board[x][y] != 0: # 총 있을 시
        if gun[idx]: # 총 소유 시
            mx = max(g_board[x][y])
            if gun[idx] < mx:
                tmp = gun[idx]
                gun[idx] = mx
                g_board[x][y].append(tmp)
                g_board[x][y].remove(mx)
        else: # 총 미소유 시
            mx = max(g_board[x][y])
            gun[idx] = mx
            g_board[x][y].remove(mx)

    return

for r in range(1,K+1):
    for i in range(1, M+1):
        x,y = pos[i]
        d = dir[i]
        nx,ny = x+dx[d], y+dy[d]
        if not (0<=nx<N and 0<=ny<N): # 격자 밖일 시 방향 반대
            nx,ny = x-dx[d], y-dy[d]
            dir[i] = (d+2)%4
        board[x][y] = 0
        pos[i] = (nx,ny)
        if not board[nx][ny]: # 플레이어 없을 시
            get_gun(nx,ny,i)
        else: # 플레이어 있을 시
            o = board[nx][ny] # 상대 플레이어 idx
            op = power[o] + gun[o]
            cp = power[i] + gun[i]
            diff = abs(op-cp)
            
            if op > cp: 
                winner = o
                loser = i
            elif op < cp: 
                winner = i
                loser = o
            else:
                if power[o] > power[i]: 
                    winner=o
                    loser=i
                else: 
                    winner = i
                    loser = o

            # loser
            if gun[loser]:
                lg = gun[loser]
                g_board[nx][ny].append(lg)
                gun[loser]=0
        
            d = dir[loser]
            lx,ly = pos[loser]
            while True:
                nlx,nly = lx+dx[d], ly+dy[d]
                if 0<=nlx<N and 0<=nly<N and board[nlx][nly] == 0: # 빈 칸 찾았을 시
                    pos[loser] = (nlx,nly)
                    dir[loser] = d
                    board[nlx][nly] = loser
                    get_gun(nlx,nly,loser)
                    break
                else: 
                    d = (d+1)%4
            # winner
            get_gun(nx,ny,winner)
            scores[winner] += diff

        ix,iy = pos[i]
        board[ix][iy] = i

print(*scores[1:])