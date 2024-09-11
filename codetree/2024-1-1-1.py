from collections import deque
from copy import deepcopy

K, M = map(int, input().split())
board = []

for _ in range(5):
    line = list(map(int, input().split()))
    board.append(line)

wall = deque(map(int, input().split()))
center = [
    (1,1), (1,2), (1,3),
    (2,1), (2,2), (2,3),
    (3,1), (3,2), (3,3)      
]
answer = []

def rotate(r,c,a):
    a = a//90
    for _ in range(a):
        up = tmp[r-1][c-1:c+2]
        left = [tmp[i][c-1] for i in range(r-1, r+2)]
        right = [tmp[i][c+1] for i in range(r-1, r+2)]
        down = tmp[r+1][c-1:c+2]
        j = 0
        for i in range(c-1, c+2):
            tmp[r-1][i] = left[j]
            j+=1
        j = 0
        for i in range(r-1, r+2):
            tmp[i][c+1] = up[j]
            j+=1
        j = 0
        for i in range(c+1,c-2,-1):
            tmp[r+1][i] = right[j]
            j+=1
        j = 0
        for i in range(r-1, r+2):
            tmp[i][c-1] = down[j]
            j+=1          
    
    return

def find():
    q = deque()
    visited = deque()

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0

    for i in range(5):
        for j in range(5):
            if tmp[i][j] != 0:
                q.append((i,j))
                visited.append((i,j))
                m=1
                while q:
                    x,y = q.popleft() 
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5 and (nx,ny) not in visited:
                            if tmp[x][y] == tmp[nx][ny]:
                                q.append((nx,ny))
                                visited.append((nx,ny))
                                m+=1
                if m > 2:
                    cnt+=len(visited)
                    while visited:
                        x,y = visited.popleft()
                        tmp[x][y] = 0
                else: visited.clear()
    
    return cnt          

def print_board(board):
    for line in board:
        print(line)
    print()

for I in range(K):
    max_value = -1
    angle = 0
    coor = (0,0)
    for r,c in center:
        tmp = deepcopy(board)
        rotate(r,c, 90)
        score = find()
        if score > max_value:
            max_value = score
            angle = 90
            coor = (r,c)
            rotated = tmp
        elif score == max_value:
            if 90 < angle: 
                angle = 90
                coor = (r,c)
                rotated = tmp
            elif angle == 90 and c < coor[1]:
                coor = (r,c)
                rotated = tmp
            elif angle == 90 and  c == coor[1] and r < coor[0]:
                coor = (r,c)
                rotated = tmp

        tmp = deepcopy(board)
        rotate(r,c, 180)
        score = find()
        if score > max_value:
            max_value = score
            angle = 180
            coor = (r,c)
            rotated = tmp
        elif score == max_value:
            if 180 < angle: 
                angle = 180
                coor = (r,c)
                rotated = tmp
            elif angle == 180 and c < coor[1]:
                coor = (r,c)
                rotated = tmp
            elif angle == 180 and  c == coor[1] and r < coor[0]:
                coor = (r,c)
                rotated = tmp

        tmp = deepcopy(board)
        rotate(r,c, 270)
        score = find()
        if score > max_value:
            max_value = score
            angle = 270
            coor = (r,c)
            rotated = tmp
        elif score == max_value:
            if angle == 270 and c < coor[1]:
                coor = (r,c)
                rotated = tmp
            elif angle == 270 and  c == coor[1] and r < coor[0]:
                coor = (r,c)
                rotated = tmp
    
    score = max_value
    if score == 0: break
    tmp = rotated

    while True:
        for p in range(5):
            for q in range(4, -1, -1):
                if tmp[q][p] == 0:
                    n = wall.popleft()
                    tmp[q][p] = n
        result = find()
        if result == 0 : break
        score += result
        
    board = tmp

    print(score, end=' ')
        