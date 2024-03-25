"""
bfs
"""

"""
연구소 크기: N x M
0: 빈 칸
1: 벽
2: 바이러스
벽 3개 세울 수 있음
얻을 수 있는 안전 영역의 최대 크기 구하기
"""

from collections import deque
from itertools import combinations
import copy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
room = []
num = 0

for _ in range(N):
    room.append(list(map(int, input().split())))

def bfs(room):
    virus = deque([(r,c) for r in range(N) for c in range(M) if room[r][c] == 2]) # 바이러스가 있는 좌표 queue
    while virus:
        r,c = virus.popleft()
        for dr, dc in zip([r, r, r+1, r-1], [c+1, c-1, c, c]): # 상하좌우 탐색
            if 0 <= dr < N and 0 <= dc < M and room[dr][dc] == 0: # room 좌표 안에 있고 현재는 바이러스가 없을 경우
                room[dr][dc] = 2
                virus.append((dr, dc))
    
    cnt = sum(line.count(0) for line in room)
    
    global num
    num = max(num, cnt)

empty = [(r,c) for r in range(N) for c in range(M) if room[r][c] == 0] # 빈 칸인 좌표 list
for coor in combinations(empty, 3):
    test_room = copy.deepcopy(room)
    for r, c in coor:
        test_room[r][c] = 1
    bfs(test_room)

print(num)