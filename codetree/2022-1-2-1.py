"""
특정 루트를 순회할 때 단순히 빈칸을 찾아 이동할 경우,
그 루트를 모두 채우고 있을 때는 오류가 생김.
꼬리를 먼저 비운다음 머리를 채우는 식으로
"""

from collections import deque

N,M,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
teams = {}
team_n = 5

v = [[0]*N for _ in range(N)]
ans = 0

def bfs(sx,sy):
    global board, v, team_n

    q = deque()
    q.append((sx,sy))

    v[sx][sy] = 1

    team = deque()
    team.append((sx,sy))

    board[sx][sy] = team_n

    while q:
        x,y = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and not v[nx][ny]: 
                if board[nx][ny] == 2 or ((x,y)!=(sx,sy) and board[nx][ny] == 3): 
                    q.append((nx,ny))
                    v[nx][ny] = 1
                    team.append((nx,ny))
                    board[nx][ny] = team_n
    
    teams[team_n] = team

    return

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            bfs(i,j)
            team_n+=1

for r in range(K):
    # 머리 사람 이동
    for team in teams.values():
        tx,ty = team.pop() # 꼬리사람
        board[tx][ty] = 4
        hx, hy = team[0] # 머리사람
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx,ny = hx+dx, hy+dy
            if 0<=nx<N and 0<=ny<N and board[nx][ny] == 4:
                team.appendleft((nx,ny))
                board[nx][ny] = board[hx][hy]
                break

    # 공 이동
    r = r%(4*N)
    if 0<=r<N:
        for i in range(N):
            if board[r][i] > 4: 
                num = board[r][i]
                ans += (teams[num].index((r,i))+1)**2
                teams[num].reverse()
                break
    elif N<=r<2*N:
        for i in range(N-1,-1,-1):
            if board[i][r%N] > 4:
                num = board[i][r%N]
                ans += (teams[num].index((i,r%N))+1)**2
                teams[num].reverse()
                break
    elif 2*N<=r<3*N:
        for i in range(N-1,-1,-1):
            if board[N-r%N-1][i] > 4:
                num = board[N-r%N-1][i]
                ans += (teams[num].index((N-r%N-1,i))+1)**2
                teams[num].reverse()
                break
    elif 3*N<=r<4*N:
        for i in range(N):
            if board[i][N-r%N-1] > 4:
                num = board[i][N-r%N-1]
                ans += (teams[num].index((i, N-r%N-1))+1)**2
                teams[num].reverse()
                break

print(ans)