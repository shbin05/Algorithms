from copy import deepcopy
from collections import deque

N,M,F = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board_3d = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]
f = [list(map(int, input().split())) for _ in range(F)]

# 최종 출구
bex,bey = -1,-1

# 공간 시작 지점
bsx,bsy = -1,-1

# 공간 시작 방향
bsd = -1 # 0,1,2,3 북동남서

# 정육면체 벽 시작하는 공간 내 좌표
wbx,wby = -1,-1

# 정육면체 내 출구 좌표
wex,wey = -1,-1

# 출발 위치
sx,sy = -1,-1

for i in range(N):
    for j in range(N):
        if board[i][j] == 4: 
            bex,bey = i,j
        elif board[i][j]==3 and (wbx,wby)==(-1,-1):
            wbx,wby = i,j

# 공간 시작 지점 방향 찾기
for i in range(wbx-1,wbx+M+1):
    for j in range(wby-1,wby+M+1):
        if board[i][j] == 0:
            bsx,bsy = i,j
            if i==wbx-1: bsd = 0
            elif j==wby+M: bsd = 1
            elif i==wbx+M: bsd = 2
            elif j==wby-1: bsd = 3

# 정육면체 정리
# 북 - 2번 회전
b = board_3d[3]
for _ in range(2):
    cb = deepcopy(b)
    for i in range(M):
        for j in range(M):
            cb[i][j] = b[M-j-1][i]
    b = cb
board_3d[3] = b
# 동 - 3번 회전
b = board_3d[0]
for _ in range(3):
    cb = deepcopy(b)
    for i in range(M):
        for j in range(M):
            cb[i][j] = b[M-j-1][i]
    b = cb
board_3d[0] = b
# 서 - 1번 회전
b = board_3d[1]
cb = deepcopy(b)
for i in range(M):
    for j in range(M):
        cb[i][j] = b[M-j-1][i]
board_3d[1] = cb

# 정육면체 평면에 펼치기
wall = [[9]*(3*M) for _ in range(3*M)]
for i in range(3*M):
    for j in range(3*M):
        if 0<=i<M:
            if M<=j<2*M: wall[i][j] = board_3d[3][i][j-M]
        elif M<=i<2*M:
            if 0<=j<M: wall[i][j] = board_3d[1][i-M][j]
            elif M<=j<2*M: wall[i][j] = board_3d[4][i-M][j-M]
            else: wall[i][j] = board_3d[0][i-M][j-2*M]
        else:
            if M<=j<2*M: wall[i][j] = board_3d[2][i-2*M][j-M]

        if wall[i][j]==2: sx,sy = i,j

# 정육면체에 출구 좌표 구하기
if bsd==0: #북
    for i in range(3*M):
        if wall[0][i]==0: 
            wex,wey = 0,i

elif bsd==1: #동
    for i in range(3*M):
        if wall[i][-1]==0:
            wex,wey = i,3*M-1

elif bsd==2: #남
    for i in range(3*M):
        if wall[3*M-1][i]==0:
            wex,wey = 3*M-1,i
else: #서
    for i in range(3*M):
        if wall[i][0]==0:
            wex,wey = i,0


def find_we():
    q = deque()
    q.append((sx,sy))

    visited = deque()
    
    counts = [[0]*(3*M) for _ in range(3*M)]

    while q:
        x,y = q.popleft()
        if (x,y)==(wex,wey):
            break
        for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<3*M and 0<=ny<3*M:
                if (nx,ny) not in visited:
                    if wall[nx][ny]==0:
                        q.append((nx,ny))
                        visited.append((nx,ny))
                        counts[nx][ny]=counts[x][y]+1
                    elif wall[nx][ny]==9:
                        # 1사분면 혹은 4사분면
                        if (y==M and 0<=x<M) or (x==M and 0<=y<M) or (y==2*M-1 and 2*M<=x<3*M) or (x==2*M-1 and 2*M<=y<3*M):
                            nx,ny = y,x
                            if wall[nx][ny]==0 and (nx,ny) not in visited:
                                q.append((nx,ny))
                                visited.append((nx,ny))
                                counts[nx][ny]=counts[x][y]+1
                        else:
                            if y==2*M-1 and 0<=x<M: # 2사분면
                                nx,ny = M, 3*M-1-x
                            elif x==M and 2*M<=y<3*M: # 2사분면
                                nx,ny = 3*M-1-y, 2*M-1
                            elif x==2*M-1 and 0<=y<M: # 3사분면
                                nx,ny = 3*M-1-y, M
                            else: # 3사분면
                                nx,ny = 2*M-1, 3*M-1-x
                            if wall[nx][ny]==0 and (nx,ny) not in visited:
                                q.append((nx,ny))
                                visited.append((nx,ny))
                                counts[nx][ny]=counts[x][y]+1
    
    return counts[wex][wey]

def find_e():
    q = deque()
    q.append((bsx,bsy))

    visited = deque()

    counts = [[0]*N for _ in range(N)]
    counts[bsx][bsy]=t+1

    while q:
        x,y = q.popleft()
        if (x,y)==(bex,bey):
            break
        for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and not (nx,ny) in visited:
                if board[nx][ny]==0 or board[nx][ny]==4:
                    if strange[nx][ny]==0 or counts[x][y]<strange[nx][ny]-1:
                        q.append((nx,ny))
                        visited.append((nx,ny))
                        counts[nx][ny] = counts[x][y]+1
    
    return counts[bex][bey]

# 시간 이상현상 표시
strange = [[0]*N for _ in range(N)]
for r,c,d,v in f:
    board[r][c]=1
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    dr,dc = dir[d]
    nr,nc = r+dr,c+dc
    turn = 1
    while 0<=nr<N and 0<=nc<N and board[nr][nc]==0:
        strange[nr][nc]=v*turn
        nr,nc = nr+dr,nc+dc
        turn+=1

# 정육면체 이동
t = find_we()
# 정육면체 탈출 성공 시
t = find_e()

if t>0: print(t)   
else: print(-1) 