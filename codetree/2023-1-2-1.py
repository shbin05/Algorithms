from copy import deepcopy

N,M,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    x,y = map(lambda x: int(x)-1, input().split())
    board[x][y] -= 1
ex,ey = map(lambda x: int(x)-1, input().split())
board[ex][ey] = -11

moved = 0
escaped = 0

def find_square():
    l = 2
    while True:
        sx = ex-l+1
        sy = ey-l+1

        for i in range(sx, sx+l):
            for j in range(sy, sy+l):
                if i>=0 and i+l-1<N and j>=0 and j+l-1<N:
                    for x in range(i, i+l):
                        for y in range(j, j+l):
                            if -11 < board[x][y] < 0:
                                return i, j, l
        l+=1

def rotate(sx, sy, l):
    nboard = deepcopy(board)
    for i in range(l):
        for j in range(l):
            nboard[sx+i][sy+j] = board[sx+l-j-1][sy+i]
            if nboard[sx+i][sy+j] > 0: nboard[sx+i][sy+j] -= 1
    
    return nboard

def update_exit():
    global ex,ey
    for i in range(N):
        for j in range(N):
            if board[i][j] == -11:
                ex, ey = i,j
    
    return

for _ in range(K):
    nboard = deepcopy(board)
    # 유저 이동
    for i in range(N):
        for j in range(N):
            if -11 < board[i][j] < 0: # 유저 있는 칸일 시 이동 진행
                cur_dist = abs(ex-i) + abs(ey-j)
                for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni,nj = i+dx, j+dy
                    if 0 <= ni < N and 0 <= nj < N and board[ni][nj] <= 0: # 범위 안이고, 벽이 아닐 경우
                        n_dist = abs(ex-ni) + abs(ey-nj)
                        if n_dist < cur_dist:
                            moved -= board[i][j]
                            nboard[i][j] -= board[i][j]
                            if nboard[ni][nj] != -11: # 출구가 아닐 경우
                                nboard[ni][nj] += board[i][j] 
                            if nboard[ni][nj] == -11:
                                escaped -= board[i][j]
                            break
    if escaped == M: break # 모든 유저 탈출 시 즉시 종료
    board = nboard
    sx, sy, l = find_square()
    board = rotate(sx,sy,l)
    update_exit()

print(moved)
print(ex+1, ey+1)