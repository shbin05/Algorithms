"""
현재 위치에서 목표 지점까지의 최단거리를 구할 때,
최단 거리를 위한 다음 위치를 구하기 위해서는
거꾸로 목표 지점에서 현재 위치까지의 최단거리를 구해주는 것이 필요함!!!

꼭 다시 풀어보기
"""

from collections import deque

N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
stores = [()]+[tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
people = [() for _ in range(M+1)]
arrived = [False]*(M+1)
bc = set()

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            bc.add((i,j))
            board[i][j] = 0

def find(sx,sy,dests): # 최단 경로 탐색
    q = deque()
    v = [[0]*N for _ in range(N)]

    q.append((sx,sy))
    v[sx][sy] = 1

    li = []
    while q:
        nq = deque()
        for x,y in q:
            if (x,y) in dests:
                li.append((x,y))
            else:
                for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    nx,ny = x+dx, y+dy
                    if 0<=nx<N and 0<=ny<N and board[nx][ny]==0 and v[nx][ny]==0:
                        nq.append((nx,ny))
                        v[nx][ny] = v[x][y]+1
        if len(li)>0:
            li.sort()
            return li[0]
        q=nq

    return

q = deque()
t = 1
while q or t==1:
    nq = deque()
    banned = []

    for x,y,m in q:
        if arrived[m]: continue
        sx,sy = stores[m]
        dests = set(((x-1,y),(x+1,y),(x,y-1),(x,y+1)))
        nx,ny = find(sx,sy,dests)
        if (nx,ny)==(sx,sy):
            arrived[m] = t
            banned.append((sx,sy))
        else:
            nq.append((nx,ny,m))
    q=nq

    for x,y in banned:
        board[x][y] = 1

    if t<=M:
        sx,sy = stores[t]
        bx,by = find(sx,sy,bc)
        bc.remove((bx,by))
        board[bx][by] = 1
        q.append((bx,by,t))

    t+=1

print(max(arrived))