"""
구현
"""

"""
좌표: (r,c), 1부터 시작
공기 청정기는 항상 1열에 있고, 크기는 두 행 차지
(r,c)에 있는 미세먼지의 양은 A(r,c)
공기 청정기가 있는 곳은 A(r,c)가 -1

(r,c)에 있는 미세먼지는 인접한 네 방향으로 확산
인접한 방향에 공기청정기가 있거나, 칸이 없으면 확산 x
확산되는 양은 A(r,c)//5
(r,c)에는 미세먼지가 A(r,c) - A(r,c)//5 만큼 남아있음

위쪽 공기청정기 바람은 반시계 방향으로 순환, 아래쪽 공기청정기 바람은 시계방향으로 순환
바람이 불면 미세먼지가 바람 방향대로 한 칸씩 이동

T초가 지난 후 방에 남아있는 미세먼지의 양 구하기
"""
from collections import deque

r,c,t = map(int, input().split())

room = []
dirt = deque()
fresher = []
for i in range(r):
    line = list(map(int, input().split()))
    if line[0] == -1: fresher.append(i)
    for j in range(c):
        if line[j] > 0: dirt.append((i,j,line[j]))
    room.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(t):
    for _ in range(len(dirt)): # 먼지 확산
        x,y,d = dirt.popleft()
        s = d//5 # 확산되는 먼지의 양
        if s==0: continue
        else:
            cnt = 0
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1: 
                    cnt+=1
                    room[nx][ny] += s
            room[x][y] -= cnt*s

    # 반시계 순환
    x,y = fresher[0], 1

    prev = 0
    while y+1 < c:
        tmp = room[x][y]
        room[x][y] = prev
        prev = tmp
        y+=1

    while x > 0:
        tmp = room[x][y]
        room[x][y] = prev
        prev = tmp
        x-=1
    
    while y > 0:
        tmp = room[x][y]
        room[x][y] = prev
        prev = tmp
        if y == 1: 
            y-=1
            break
        y-=1

    while x < fresher[0]:
        tmp = room[x][y]
        room[x][y] = prev
        prev = tmp
        x+=1
    
    # 시계 방향 순환
    x,y = fresher[1], 1

    prev = 0
    while y+1 < c:
        tmp = room[x][y]
        room[x][y] = prev
        prev = tmp
        y+=1

    while x+1 < r:
        tmp = room[x][y]
        room[x][y] = prev
        prev = tmp
        x+=1
    
    while y > 0:
        tmp = room[x][y]
        room[x][y] = prev
        prev = tmp
        if y == 1: 
            y-=1
            break
        y-=1

    while x > fresher[1]:
        tmp = room[x][y]
        room[x][y] = prev
        prev = tmp
        x-=1
    
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0: dirt.append((i,j,room[i][j]))

cnt = 0
for _ in range(len(dirt)):
    _,_,d = dirt.popleft()
    cnt+=d

print(cnt)