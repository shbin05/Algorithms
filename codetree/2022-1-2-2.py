from copy import deepcopy
from collections import deque

N,M,K,C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
kill = [[0]*N for _ in range(N)]

killed = 0

for year in range(1, M+1):
    # 나무 성장 및 번식
    nboard = deepcopy(board)
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0: # 나무 발견 시
                t = 0
                spread = deque()
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<N and 0<=ny<N:
                        if board[nx][ny] > 0: t+=1 # 인접 칸 나무 구하기
                        elif board[nx][ny] == 0 and year > kill[nx][ny]: # 인접 빈칸 및 제초제 없는 칸 구하기
                            spread.append((nx,ny))
                nboard[x][y] += t # 나무 성장
                if spread:
                    s = nboard[x][y] // len(spread)
                    for nx,ny in spread: # 번식
                        nboard[nx][ny] += s
    board = nboard

    # 제초제 뿌리기
    mx = 0
    mx_x, mx_y = 0,0
    k = deque()
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0: # 나무 발견 시
                s = board[x][y]
                t = deque()
                t.append((x,y))
                for dx,dy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                    for z in range(1,K+1):
                        nx,ny = x+dx*z, y+dy*z
                        if 0<=nx<N and 0<=ny<N:
                            if board[nx][ny] <= 0: # 벽이거나 빈 칸인 경우 
                                t.append((nx,ny))
                                break
                            s+=board[nx][ny]
                            t.append((nx,ny))
                            
                if s > mx:
                    mx = s
                    mx_x,mx_y = x,y
                    k = t
    
    for x,y in k:
        if board[x][y] > 0: board[x][y] = 0
        kill[x][y] = year+C
    
    killed += mx

print(killed)                