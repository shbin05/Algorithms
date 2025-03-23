from copy import deepcopy
from collections import deque

K,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]
center = [
    (1,1),(2,1),(3,1),
    (1,2),(2,2),(3,2),
    (1,3),(2,3),(3,3)
]
wall = deque(map(int,input().split()))

def in_board(x,y):
    if 0<=x<5 and 0<=y<5:
        return True
    else: return False

def rotate(board,x,y):
    c_board = deepcopy(board)
    sx=x-1
    sy=y-1

    for i in range(3):
        for j in range(3):
            c_board[sx+i][sy+j] = board[sx+3-j-1][sy+i]
    
    return c_board

def find(board):
    found = set()
    for x in range(5):
        for y in range(5):
            q = deque()
            q.append((x,y))
            visited = deque()
            tmp_found = []
            
            while q:
                cx,cy = q.popleft()
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx,ny = cx+dx,cy+dy
                    if in_board(nx,ny) and board[cx][cy] == board[nx][ny] and (nx,ny) not in visited:
                        q.append((nx,ny))
                        visited.append((nx,ny))
                        tmp_found.append((nx,ny))

            if len(tmp_found) >= 3:
                for tx,ty in tmp_found:
                    found.add((tx,ty))
    
    return found


for turn in range(K):

    cnt = 0

    max_found = 0
    tmp_board = list()
    tmp_found = set()
    tmp_angle=270

    for x,y in center:
        c_board = deepcopy(board)
        b90 = rotate(c_board,x,y)
        f90 = find(b90)
        if len(f90) > max_found:
            max_found = len(f90)
            tmp_found = f90
            tmp_board = b90
            tmp_angle = 90
        elif len(f90) == max_found and 90 < tmp_angle:
            max_found = len(f90)
            tmp_found = f90
            tmp_board = b90
            tmp_angle = 90

        b180 = rotate(b90,x,y)
        f180 = find(b180)
        if len(f180) > max_found:
            max_found = len(f180)
            tmp_found = f180
            tmp_board = b180
            tmp_angle = 180
        elif len(f180) == max_found and 180 < tmp_angle:
            max_found = len(f180)
            tmp_found = f180
            tmp_board = b180
            tmp_angle = 180
        
        b270 = rotate(b180,x,y)
        f270 = find(b270)
        if len(f270) > max_found:
            max_found = len(f270)
            tmp_found = f270
            tmp_board = b270
            tmp_angle = 270
    
    if(max_found) == 0:
        break

    board = tmp_board
    found = tmp_found
    found = sorted(found, key=lambda x: (x[1], -x[0]))
    cnt += len(found)

    for x,y in found:
        board[x][y] = wall.popleft()
    
    while True:
        found = find(board)
        if len(found) == 0: break
        
        found = sorted(found, key=lambda x: (x[1], -x[0]))
        cnt+=len(found)
        for x,y in found:
            board[x][y] = wall.popleft()
    
    print(cnt, end=' ')

