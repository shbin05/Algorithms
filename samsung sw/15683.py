"""
dfs
"""

"""
1: >
2: < >
3: ^ >
4: < ^ >

5:   ^
   <   >
     v
6: 벽
-1: cctv 시야
"""

from copy import deepcopy

n, m = map(int, input().split())
room = []
cctv = []

for i in range(n):
    line = list(map(int, input().split()))
    room.append(line)
    for j in range(m):
        if line[j] in [1, 2, 3, 4, 5]:
            cctv.append([line[j], i, j])

minimum = float("inf")

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mode = [
    [],
    [[0], [1], [2], [3]], # 1번 카메라
    [[0, 2], [1, 3]], # 2번 카메라
    [[0, 1], [1, 2], [2, 3], [3, 0]], # 3번 카메라
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번 카메라
    [[0, 1, 2, 3]] # 5번 카메라
]

def fill(room, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 방 밖이면 중단
                break

            if room[nx][ny] == 6: # 벽이면 중단
                break
            elif room[nx][ny] == 0:
                room[nx][ny] = -1


def dfs(depth, room):
    global minimum
    if depth == len(cctv):
        cnt = 0
        for line in room:
            cnt += line.count(0)
        minimum = min(minimum, cnt)
        return
    
    copied = deepcopy(room)
    num, x, y = cctv[depth]

    for i in mode[num]:
        fill(copied, i , x, y)
        dfs(depth+1, copied)
        copied = deepcopy(room)

dfs(0, room)
print(minimum)