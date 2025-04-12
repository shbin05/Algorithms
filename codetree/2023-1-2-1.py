from copy import deepcopy

N,M,K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j]>0:
            board[i][j].append(line[j])
players = []
for i in range(M):
    x,y = map(int,input().split())
    x,y = x-1,y-1
    players.append((x,y))
    board[x][y].append(i+11)
ex,ey = map(int,input().split())
ex,ey = ex-1,ey-1
board[ex][ey].append(-1)

escaped = [0]*M
moved_sum=0

def in_board(x,y):
    if 0<=x<N and 0<=y<N: return True
    else: False

def rotate(size, sx, sy):
    global board, ex, ey

    cboard = deepcopy(board)
    for i in range(size):
        for j in range(size):
            cboard[sx+i][sy+j] = board[sx+size-j-1][sy+i]
    # 순회하며 유저 좌표, 출구 좌표, 벽 정보 업데이트
    for i in range(sx,sx+size):
        for j in range(sy,sy+size):
            if len(cboard[i][j]) > 0:
                # 유저인 경우
                if cboard[i][j][0]>=11:
                    for idx in cboard[i][j]:
                        players[idx-11]=(i,j)
                # 출구인 경우
                elif cboard[i][j][0]==-1:
                    ex,ey = i,j
                # 벽인 경우
                elif 1<=cboard[i][j][0]<=9:
                    cboard[i][j][0] -= 1
                    # 벽 내구도 0일 경우
                    if cboard[i][j][0] == 0:
                        cboard[i][j].pop()
    
    board = cboard
    return

for t in range(K):
    # 참가자 이동 구현
    for i, (px,py) in enumerate(players):
        if escaped[i]==1: continue # 탈출한 유저 제외
        dist=abs(ex-px)+abs(ey-py)
        npx,npy=px,py
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=px+dx,py+dy
            # 보드 안이고, 벽 없거나 참가자이거나 출구일 경우 이동
            if in_board(nx,ny) and (len(board[nx][ny])==0 or board[nx][ny][0]>=11 or board[nx][ny][0]==-1): 
                ndist=abs(ex-nx)+abs(ey-ny)
                if ndist < dist:
                    dist=ndist
                    npx,npy = nx,ny
        # 이동했을 경우 업데이트
        if (npx,npy)!=(px,py):
            moved_sum+=1
            board[px][py].remove(i+11)
            board[npx][npy].append(i+11)
            players[i]=(npx,npy)

            # 출구 도착했을 경우
            if players[i]==(ex,ey): 
                escaped[i] = 1
                board[ex][ey].remove(i+11)

    # 모두 탈출하면 종료
    if escaped.count(0) == 0: break

    # 미로 회전
    # 크기가 2인 정사각형부터 차례로 탐색
    size=2
    found = False
    while True:
        # 정사각형 시작점
        for sx in range(0,N-size+1):
            for sy in range(0,N-size+1):
                # 출구 포함되었는지 확인
                if sx<=ex<sx+size and sy<=ey<sy+size:
                    # 정사각형 내부
                    for i in range(sx,sx+size):
                        for j in range(sy,sy+size):
                            # 플레이어 존재하는지 확인
                            if len(board[i][j])>0 and board[i][j][0]>=11:
                                rotate(size,sx,sy)
                                found = True
                                break
                        if found: break
                    if found: break
                if found: break
            if found: break
        if found: break
        size+=1

print(moved_sum)
print(ex+1,ey+1)