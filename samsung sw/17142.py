"""
bfs
"""

"""
가장 처음에 모든 바이러스는 비활성 상태, 
활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제됨 (1초동안)

연구소의 바이러스 M개를 활성 상태로 변경하려고 함

연구소 크기: n x n
0은 빈 칸, 1은 벽, 2는 바이러스

연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력,
어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1 출력
"""

from collections import deque
from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())

virus = []
board = []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 2: virus.append((i,j))
    board.append(line)

time_map = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1: time_map[i][j] = '-'
        elif board[i][j] == 2: time_map[i][j] = '*'
        else: time_map[i][j] = -1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(virus):
    virus = deque(virus)

    board = deepcopy(time_map)
    for x,y in virus:
        board[x][y] = 0

    max_value = 0

    while virus:
        x,y = virus.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == -1:
                    board[nx][ny] = board[x][y] + 1
                    max_value = max(max_value, board[nx][ny])
                    virus.append((nx,ny))
                elif board[nx][ny] == '*':
                    board[nx][ny] = board[x][y]+1
                    virus.append((nx,ny))

    for line in board:
        if -1 in line: return -1
        
    return max_value

times = []
for c in combinations(virus, m):
    times.append(bfs(c))

if sum(times) == -1 * len(times): print(-1)
else:
    times = [time for time in times if time!=-1]
    print(min(times))