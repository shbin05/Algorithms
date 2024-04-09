"""
bfs
"""

"""
땅 크기: n x n
국경선을 공유하는 두 나라 인구 차이가 L명 이상, R명 이하라면 국경선을 하루동안 엶
국경선이 열려있으면 그 나라는 하루동안은 연합
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수), 소수점 버림

인구 이동이 며칠 동안 발생하는지 구하기
"""

from collections import deque

n, l, r = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x,y))

    union = []
    union.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if visited[nx][ny] == True: continue
            if (l <= abs(population[x][y]-population[nx][ny]) <= r):
                visited[nx][ny] = True
                q.append((nx,ny))
                union.append((nx,ny))

    return union

day = 0
while True:
    visited = [[False]*n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] = True
                union = bfs(i,j)
                if len(union) > 1:
                    flag = True
                    pop = sum([population[x][y] for x, y in union]) // len(union)
                    for x, y in union: 
                        population[x][y] = pop
    if flag == False: break
    day+=1                

print(day)
