"""
bfs
"""

"""
n x n 공간에 물고기 m마리, 아기 상어 1마리
한 칸에 물고기 최대 1마리 존재

처음 아기 상어 크기 2,
1초에 상하좌우로 한 칸씩 이동

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없음
자신의 크기보다 작은 물고기만 먹을 수 있음 (크기 같으면 먹진 못하고 지나가기만 됨)

더 이상 먹을 수 있는 물고기가 없으면 엄마 상어에게 도움 요청
거리가 가장 가까운 물고기부터 먹으러 감, 거리가 같다면 가장 위쪽, 가장 왼쪽에 있는 물고기 먹음

이동은 1초 걸리고, 자신의 크기와 같은 수의 물고기를 먹으면 크기 1 증가
몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 먹을 수 있는지

0: 빈 칸
1,2,3,4,5,6: 물고기 크기
9: 아기 상어 위치
"""

from collections import deque

n = int(input())
space = []
size = 2

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 9: 
            x = i
            y = j
    
    space.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global size

    q = deque()
    q.append((x, y))

    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True

    # 거리 저장 배열
    distance = [[0]*n for _ in range(n)]
    candidate = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if space[nx][ny] <= size:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y]+1
                    
                    if space[nx][ny] < size and space[nx][ny] != 0:
                        candidate.append((nx, ny, distance[nx][ny]))

    return sorted(candidate, key = lambda x: (x[2], x[0], x[1])) # distance, x, y 값 기준으로 정렬

time = 0
cnt = 0
while True:
    candidate = bfs(x,y)
    if len(candidate) == 0: break

    nx, ny, distance = candidate.pop(0)
    time += distance

    space[x][y] = 0
    space[nx][ny] = 0

    x,y = nx,ny
    cnt+=1
    if cnt == size:
        size+=1
        cnt = 0

print(time)