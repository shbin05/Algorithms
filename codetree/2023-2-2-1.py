N, M, P, C, D = map(int, input().split())

rx, ry = map(lambda x: int(x)-1, input().split())

santa = [[] for _ in range(P+1)]
for i in range(1, P+1):
    i, x, y = map(int, input().split())
    x, y = x-1, y-1
    santa[i] = (x,y)

board = [[0]*N for _ in range(N)]
for i in range(1,P+1):
    x,y = santa[i]
    board[x][y] = i

stun = [0]*(P+1)
alive = [True]*(P+1)
score = [0]*(P+1)

def move_s(si, sx, sy, dx, dy, num): # 이동해야 하는 산타, 현재 위치, 이동 방향, 이동량
    global santa
    # 새로운 위치
    nsx = sx + dx*num
    nsy = sy + dy*num
    santa[si] = (nsx, nsy)

    # 탈락 여부 체크
    if 0 <= nsx < N and 0 <= nsy < N:
        # 산타와 충돌 여부 체크
        if board[nsx][nsy] == 0:
            if board[sx][sy] == si: board[sx][sy] = 0
            board[nsx][nsy] = si
        else:
            nsi = board[nsx][nsy]
            if board[sx][sy] == si: board[sx][sy] = 0
            board[nsx][nsy] = si
            move_s(nsi, nsx, nsy, dx, dy, 1)

    else:
        alive[si] = False
        if board[sx][sy] == si: board[sx][sy] = 0

    # 루돌프와 충돌 여부 체크
    if nsx == rx and nsy == ry:
        stun[si] = turn+1
        score[si] += D
        move_s(si, nsx, nsy, -dx, -dy, D)

    return

def move_r():
    global rx, ry

    min_dist = 1e+9
    tsx, tsy = 0,0 # 가장 가까운 산타 x,y 저장
    dx, dy = 0,0 # 루돌프 이동방향 저장
    for i in range(1, P+1): 
        if alive[i]==False: continue
        sx, sy = santa[i]
        dist = (rx-sx)**2 + (ry-sy)**2
        if  dist < min_dist:
            min_dist = dist
            tsx, tsy = sx, sy
        elif dist == min_dist:
            if sx > tsx:
                tsx = sx
                tsy = sy
            elif sx == tsx and sy > tsy:
                tsx = sx
                tsy = sy
    
    # 루돌프 한칸 이동
    if tsx > rx: dx +=1
    elif tsx < rx: dx -=1

    if tsy > ry: dy +=1
    elif tsy < ry: dy -=1

    rx += dx
    ry += dy

    # 산타와 충돌
    if board[rx][ry] != 0:
        stun[board[rx][ry]] = turn+1
        score[board[rx][ry]] += C
        move_s(board[rx][ry], rx, ry, dx, dy, C)

for turn in range(1, M+1):
    if alive[1:].count(True) == 0: break
    move_r()
    for i in range(1, P+1):
        if stun[i] >= turn or not alive[i]: continue
        # 루돌프와 가장 가까운 방향 탐색
        sx, sy = santa[i]
        min_dist = (rx-sx)**2 + (ry-sy)**2
        mdx, mdy = 0,0
        for dsx, dsy in [(-1,0),(0,1),(1,0),(0,-1)]:
            nsx = sx + dsx
            nsy = sy + dsy
            if 0 <= nsx < N and 0 <= nsy < N and board[nsx][nsy] == 0:
                dist = (nsx-rx)**2 + (nsy-ry)**2
                if dist < min_dist:
                    min_dist = dist
                    mdx, mdy = dsx, dsy
        
        if mdx != 0 or mdy != 0:
            move_s(i, sx, sy, mdx, mdy, 1)
    
    # 살아남은 산타 1점씩 추가
    for i in range(1, P+1):
        if alive[i]: score[i]+=1

print(*score[1:])
