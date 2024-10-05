from collections import deque

N,M,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

a_turn = [[0]*M for _ in range(N)]

def bfs(sx,sy,ex,ey):
    global board, a_set

    q = deque()
    q.append((sx,sy))

    v = [[() for _ in range(M)] for _ in range(N)]

    while q:
        x,y = q.popleft()

        if (x,y) == (ex,ey):
            board[ex][ey] = max(0, board[ex][ey]-board[sx][sy])
            cx,cy = x,y
            while True:
                bx,by = v[cx][cy]
                if (bx,by) == (sx,sy): break
                board[bx][by] = max(0, board[bx][by]-board[sx][sy]//2)
                a_set.add((bx,by))
                cx,cy = bx,by
        
            return True

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx,ny = (x+dx)%N, (y+dy)%M
            if board[nx][ny] > 0 and not v[nx][ny]:
                q.append((nx,ny))
                v[nx][ny] = (x,y)
    
    return False

def bomb(sx,sy,ex,ey):
    global board, a_set

    board[ex][ey] = max(0, board[ex][ey]-board[sx][sy])

    for dx,dy in [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]:
        nx,ny = (ex+dx)%N, (ey+dy)%M
        if (nx,ny)!=(sx,sy):
            board[nx][ny] = max(0, board[nx][ny]-board[sx][sy]//2)
            a_set.add((nx,ny))
    
    return

for turn in range(1, K+1):
    a_set = set()
    
    # 공격자 선정
    mn, mx_turn, sx, sy = 5001, 0, -1, -1
    for i in range(N):
        for j in range(M):
            if board[i][j]<=0:    continue   
            if mn>board[i][j] or (mn==board[i][j] and mx_turn<a_turn[i][j]) or \
                (mn==board[i][j] and mx_turn==a_turn[i][j] and sx+sy<i+j) or \
                (mn==board[i][j] and mx_turn==a_turn[i][j] and sx+sy==i+j and sy<j):
                mn, mx_turn, sx, sy = board[i][j], a_turn[i][j], i, j  

    # 피공격자 선정
    mx, mn_turn, ex, ey = 0, turn, N, M
    for i in range(N):
        for j in range(M):
            if board[i][j]<=0:    continue   
            if mx<board[i][j] or (mx==board[i][j] and mn_turn>a_turn[i][j]) or \
                (mx==board[i][j] and mn_turn==a_turn[i][j] and ex+ey>i+j) or \
                (mx==board[i][j] and mn_turn==a_turn[i][j] and ex+ey==i+j and ey>j):
                mx, mn_turn, ex, ey = board[i][j], a_turn[i][j], i, j  

    a_set.add((sx,sy))
    a_set.add((ex,ey))

    a_turn[sx][sy] = turn
    board[sx][sy] += N+M

    if not bfs(sx,sy,ex,ey):
        bomb(sx,sy,ex,ey)
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                cnt+=1
                if (i,j) not in a_set: board[i][j]+=1
    
    if cnt <= 1: break

print(max(map(max, board)))