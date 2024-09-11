from collections import deque

N, M, P, C, D = map(int, input().split())
rx, ry = map(int, input().split())
rx-=1
ry-=1

scores = [0]*P
stun = [0]*P
alive = [True]*P
pos = []
for _ in range(P):
    i,x,y = map(int, input().split())
    x-=1
    y-=1
    pos.append([i,x,y])
pos.sort(key = lambda x: x[0])
pos = [li[1:] for li in pos]

board = [[0]*N for _ in range(N)]
for i in range(P):
    x,y = pos[i]
    board[x][y] = i+1

def find_s():
    min_value = 1e+9
    midx = 0
    for i in range(P):
        if alive[i] == False: continue
        sx, sy = pos[i]
        dist = (rx-sx)**2 + (ry-sy)**2
        if dist < min_value:
            min_value = dist
            midx = i
        elif dist == min_value:
            if sx > pos[midx][0]:
                midx = i
            elif sx == pos[midx][0] and sy > pos[midx][1]:
                midx = i
    
    return midx

def interaction(x, y, num, dx, dy):
    global board

    tmp = board[x][y] # 기존에 있던 산타 번호

    board[x][y] = num # 밀려난 산타로 대체
    pos[num-1] = [x,y]

    nx = x + dx
    ny = y + dy
    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == 0:
            board[nx][ny] = tmp 
            pos[tmp-1] = [nx, ny]
        else:
            interaction(nx, ny, tmp, dx, dy)
    else: 
        alive[num] = False
    
    return

def move_r(idx):
    global rx, ry, board
    sx,sy = pos[idx][0], pos[idx][1]

    if sx > rx: dx = 1
    elif sx == rx: dx = 0
    else: dx = -1

    if sy > ry: dy = 1
    elif sy == ry: dy = 0
    else: dy = -1

    rx += dx
    ry += dy

    if rx == sx and ry == sy and alive[idx] == True:
        scores[idx] += C
        nsx = sx + dx*C
        nsy = sy + dy*C
        if 0 <= nsx < N and 0 <= nsy < N:
            board[sx][sy] = 0
            if board[nsx][nsy] == 0:
                board[nsx][nsy] = idx+1
                pos[idx] = [nsx, nsy]
            else: interaction(nsx, nsy, idx+1, dx, dy)
        else: 
            alive[idx] = False
            board[sx][sy] = 0
        stun[idx] = turn + 1

def move_s(idx):
    global board
    sx, sy = pos[idx][0], pos[idx][1]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    min_value = (sx-rx)**2 + (sy-ry)**2
    tmp_x, tmp_y = sx,sy
    tmp_dx, tmp_dy = 0,0
    for i in range(4):
        nsx = sx+dx[i]
        nsy = sy+dy[i]
        if 0 <= nsx < N and 0 <= nsy < N and board[nsx][nsy] == 0:
            dist = (nsx-rx)**2 + (nsy-ry)**2
            if dist < min_value:
                min_value = dist
                tmp_x, tmp_y = nsx, nsy
                tmp_dx, tmp_dy = dx[i], dy[i]
    
    board[sx][sy] = 0
    sx, sy = tmp_x, tmp_y
    board[sx][sy] = idx+1
    pos[idx] = [sx, sy]
    dx, dy = tmp_dx, tmp_dy

    if rx == sx and ry == sy and alive[idx] == True:
        scores[idx] += D
        nsx = sx - dx*D
        nsy = sy - dy*D
        if 0 <= nsx < N and 0 <= nsy < N:
            board[sx][sy] = 0
            if board[nsx][nsy] == 0:
                board[nsx][nsy] = idx+1
                pos[idx] = [nsx, nsy]
            else: interaction(nsx, nsy, idx+1, -dx, -dy)
        else: 
            alive[idx] = False
            board[sx][sy] = 0
        stun[idx] = turn + 1

def print_board(board):
    for line in board:
        print(line)
    print()

for turn in range(1, M+1):
    print(f"turn: {turn}")
    if alive.count(True) == 0: break
    idx = find_s()
    print(idx, pos[idx])
    print(f"before r move: {rx,ry}")
    print_board(board)
    move_r(idx)
    print(f"after r move: {rx,ry}")
    print_board(board)
    for i in range(P):
        if alive[i] and turn > stun[i]:
            move_s(i)
    print(f"after santa move")
    print_board(board)
    for i in range(P):
        if alive[i]: scores[i]+=1
    print(f"santa position: {pos}")

print(*scores)





