from collections import deque
from copy import deepcopy

N = int(input())
M = N//2
board = [list(map(int, input().split())) for _ in range(N)]

scores = 0

def find_group(x,y):
    global v, group_n

    q = deque()
    q.append((x,y))

    group = deque()
    group.append((x,y))

    v[x][y] = 1

    while q:
        x,y = q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] == board[x][y] and not v[nx][ny]:
                    q.append((nx,ny))
                    v[nx][ny] = 1
                    group.append((nx,ny))
    
    groups[group_n] = group
    group_n+=1

    return

def find(g1, g2):
    cnt = 0
    for x,y in g1:
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx, y+dy
            if (nx,ny) in g2: cnt+=1
    
    return cnt

def rotate(sx,sy):
    global board

    nboard = deepcopy(board)

    for i in range(M):
        for j in range(M):
            nboard[sx+i][sy+j] = board[sx+M-j-1][sy+i]

    return nboard

for r in range(4):
    # 그룹 찾기
    v = [[0]*N for _ in range(N)]
    groups={}
    group_n = 1
    for i in range(N):
        for j in range(N):
            if not v[i][j]: find_group(i,j)

    # 조화로움 계산
    for i in range(1, group_n-1):
        for j in range(i+1, group_n):
            g1 = groups[i]
            g2 = groups[j]

            boundary = find(g1,g2)
            if boundary > 0:
                blocks = len(g1) + len(g2)
                num1 = board[g1[0][0]][g1[0][1]]
                num2 = board[g2[0][0]][g2[0][1]]
                
                s = blocks * num1 * num2 * boundary

                scores += s

    if r == 3: break

    # 십자가 회전
    c1 = [board[i][M] for i in range(N)] # 세로
    c2 = [board[M][i] for i in range(N)] # 가로

    j=N-1
    for i in range(N):
        board[i][M] = c2[j]
        j-=1
    j=0
    for i in range(N):
        board[M][i] = c1[j]
        j+=1

    # 십자가 외 부분 회전
    for (sx,sy) in [(0,0),(0,M+1),(M+1,0),(M+1,M+1)]:
        board = rotate(sx,sy)

print(scores)