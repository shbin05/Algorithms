from copy import deepcopy

N,M,K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = list(map(int,input().split()))
    for j in range(N):
        if line[j]!=0:
            board[i][j].append(line[j])
users = [(0,0) for _ in range(11)]
escaped = [0]*11+[0]*M
for num in range(1, M+1):
    x,y = map(int,input().split())
    x,y = x-1,y-1
    users.append((x,y))
    board[x][y].append(num+10)
ex,ey = map(int,input().split())
ex,ey = ex-1,ey-1
board[ex][ey].append(-1)

moved = 0

for _ in range(K):
    cboard = deepcopy(board)
    for i, (x,y) in enumerate(users[11:]): # 유저 이동 
        if escaped[i+11] == 1: continue # 탈출한 유저 제외
        mdist = abs(ex-x)+abs(ey-y)
        tx,ty = x,y
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                if len(board[nx][ny]) == 0 or board[nx][ny][0] == -1 or board[nx][ny][0]>10:
                    ndist = abs(ex-nx)+abs(ey-ny)
                    if ndist < mdist: 
                        mdist = ndist
                        tx,ty = nx,ny
        # 이동했을 경우
        if (tx,ty)!=(x,y):
            moved+=1
            if (tx,ty)==(ex,ey): # 출구 도착했을 경우
                escaped[i+11] = 1
                cboard[x][y].remove(i+11)
            else:
                cboard[x][y].remove(i+11)
                cboard[tx][ty].append(i+11)
                users[i+11] = (tx,ty)

    if escaped[11:].count(0) == 0: break
    
    board = cboard
    square = ()
    size = 2
    found = False
    while not found:
        for sx in range(0,N-size+1):
            for sy in range(0,N-size+1):
                if sx<=ex<sx+size and sy<=ey<sy+size:
                    for i in range(sx,sx+size):
                        for j in range(sy,sy+size):
                            if len(board[i][j])>0 and board[i][j][0]>10:
                                found = True
                                square = (sx,sy)
                            if found: break
                        if found: break
                if found: break
            if found: break
        if found: break
        size+=1
    
    sx,sy = square
    cboard = deepcopy(board)
    for x in range(size):
        for y in range(size):
            cboard[sx+x][sy+y] = board[sx+size-y-1][sy+x]
    for x in range(size):
        for y in range(size):
            if len(cboard[sx+x][sy+y])==0: pass
            elif cboard[sx+x][sy+y][0] == -1: # 출구일 경우
                ex,ey = sx+x,sy+y
            elif 1<=cboard[sx+x][sy+y][0]<=9: # 벽일 경우
                    cboard[sx+x][sy+y][0] -= 1
                    if cboard[sx+x][sy+y][0] == 0: cboard[sx+x][sy+y].remove(0)
            else: # user 일 경우
                for idx in cboard[sx+x][sy+y]:
                    users[idx] = (sx+x,sy+y)
    board = cboard

print(moved)
print(ex+1,ey+1)