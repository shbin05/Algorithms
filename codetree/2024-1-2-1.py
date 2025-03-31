from collections import deque

def bfs(cx,cy):
    q = deque()
    q.append((cx,cy))

    visited = []
    max_v = 0

    while q:
        x,y = q.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx, y+dy
            if 0<=nx<R+3 and 0<=ny<C:
                if (nx,ny) not in visited:
                    if (abs(board[x][y]) == abs(board[nx][ny])) or (board[x][y]<0 and board[nx][ny]!=0):
                        if nx > max_v: max_v = nx
                        q.append((nx,ny))
                        visited.append((nx,ny))
    
    return max_v-2


R,C,K = map(int, input().split())
board = [[0]*C for _ in range(R+3)]

s = 0
for k in range(1,K+1):
    c,d = map(int, input().split())
    c-=1

    cx,cy = 1,c
    while True:
        # 밑으로 이동:
        if cx+2<R+3 and board[cx+2][cy]==0 and board[cx+1][cy-1]==0 and board[cx+1][cy+1]==0:
            cx+=1
        # 왼쪽 밑으로 이동:
        elif cx+2<R+3 and cy-2>=0 and board[cx-1][cy-1]==0 and board[cx][cy-2]==0 and board[cx+1][cy-1]==0 and board[cx+1][cy-2]==0 and board[cx+2][cy-1]==0:
            cx+=1
            cy-=1
            d = (d-1)%4
        # 오른쪽 밑으로 이동:
        elif cx+2<R+3 and cy+2<C and board[cx-1][cy+1]==0 and board[cx][cy+2]==0 and board[cx+1][cy+1]==0 and board[cx+2][cy+1]==0 and board[cx+1][cy+2]==0:
            cx+=1
            cy+=1
            d = (d+1)%4
        else: break

    # 비우기:
    if cx<4: 
        board = [[0]*C for _ in range(R+3)]
        continue
    
    # 골렘 표시:
    for i, (dx,dy) in enumerate([(-1,0),(0,1),(1,0),(0,-1)]):
        board[cx][cy] = k
        board[cx+dx][cy+dy] = k
        if d==i: board[cx+dx][cy+dy]=-k
    
    # 정령 이동:
    v = bfs(cx,cy)
    s+=v
    
print(s)