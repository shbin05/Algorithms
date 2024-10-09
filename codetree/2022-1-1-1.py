N,M,H,K = map(int, input().split())
fx,fy,fd = N//2, N//2, 0 # 술래 초기 위치
hide = []
dir = [] # 0,1,2,3 순서대로 상우하좌
trees = []

scores = 0

tmp_board = [[0]*N for _ in range(N)]

for _ in range(M):
    x,y,d = map(int, input().split())
    hide.append((x-1,y-1))
    dir.append(d)

for _ in range(H):
    x,y = map(int, input().split())
    trees.append((x-1,y-1))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 술래 이동 관련
cnt=0
move_d = 1
changed = False

for turn in range(1, K+1):
    move = []
    # 거리 3 이하인 도망자 선별
    for i in range(len(hide)): 
        hx,hy = hide[i] 
        if abs(fx-hx)+abs(fy-hy) <= 3: 
            move.append(i)
    # 도망자 이동
    for idx in move:
        hx,hy = hide[idx]
        d = dir[idx]
        nx,ny = hx+dx[d], hy+dy[d]
        if 0<=nx<N and 0<=ny<N:
            if (nx,ny)!=(fx,fy):
                hide[idx] = (nx,ny)
        else:
            d = (d+2)%4
            dir[idx] = d
            nx,ny = hx+dx[d], hy+dy[d]
            if (nx,ny)!=(fx,fy):
                hide[idx] = (nx,ny)
    # 술래 이동
    tmp_board[fx][fy] = 0
    fx,fy = fx+dx[fd]*move_d, fy+dy[fd]*move_d
    cnt+=1
    if cnt == 2: 
        if (fx,fy) == (N-1, 0) and not changed:
            fd = (fd+1)%4
        elif (fx,fy) == (N-1,N-1) and changed:
            fd = (fd-1)%4
            cnt = 1
        else:
            cnt = 0
            if changed: 
                fd = (fd-1)%4
                move_d -= 1
            else: 
                fd = (fd+1)%4
                move_d += 1
    else:
        if changed: fd = (fd-1)%4
        else: fd = (fd+1)%4

    if (fx,fy) == (0,0):
        changed = True
        cnt = 0
        fd = 2
    elif (fx,fy) == (N//2,N//2):
        changed = False
        cnt = 0
        fd = 0
        move_d = 1

    tmp_board[fx][fy] = 1

    # 술래 시야 체크
    found = []
    for i in range(3):
        nx,ny = fx+dx[fd]*i, fy+dy[fd]*i
        if (nx,ny) in hide and (nx,ny) not in trees:
            found.append((nx,ny))
    
    scores += turn * len(found)

    for hx,hy in found:
        idx = hide.index((hx,hy))
        hide.pop(idx)
        dir.pop(idx)

print(scores)