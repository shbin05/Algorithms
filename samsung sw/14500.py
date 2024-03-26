"""
구현
DFS
DFS를 활용한 여러 방향 탐색
"""

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

max_value = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, dsum, cnt):
    global max_value
    if cnt == 4: 
        max_value = max(max_value, dsum) # 모양이 완성되었을 떄
        return
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, dsum+board[nx][ny], cnt+1)
            visited[nx][ny] = False

def special(x, y): # ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값은 따로 계산
    global max_value
    for i in range(4):
        tmp = board[x][y] # 초기값은 시작지점 값으로
        for j in range(3):
            k = (i+j)%4
            nx = x+dx[k]
            ny = y+dy[k]

            if not (0 <= nx < n and 0 <= ny < m):
                tmp = 0
                break
            tmp += board[nx][ny]

        max_value = max(max_value, tmp)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

        special(i, j)

print(max_value)