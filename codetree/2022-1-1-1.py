N,M,H,K = map(int, input().split())
fx,fy,fd = N//2, N//2, 0 # 술래 초기 위치
hide = []
dir = [] # 0,1,2,3 순서대로 상우하좌
trees = []

scores = 0

for _ in range(M):
    x,y,d = map(int, input().split())
    hide.append((x-1,y-1))
    dir.append(d)

for _ in range(H):
    x,y = map(int, input().split())
    trees.append((x-1,y-1))

# 상우하좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 술래 이동 관련
turned=0
moved = 0
mx_move = 1
flag = False

for turn in range(1, K+1):
    move = []
    # 거리 3 이하인 도망자 선별 및 이동
    for i in range(len(hide)): 
        hx,hy = hide[i] 
        if abs(fx-hx)+abs(fy-hy) <= 3:  
            d = dir[i]
            nx,ny = hx+dx[d], hy+dy[d]
            if 0<=nx<N and 0<=ny<N:
                if (nx,ny)!=(fx,fy):
                    hide[i] = (nx,ny)
            else:
                d = (d+2)%4
                dir[i] = d
                nx,ny = hx+dx[d], hy+dy[d]
                if (nx,ny)!=(fx,fy):
                    hide[i] = (nx,ny)
    # 술래 이동
    fx,fy = fx+dx[fd], fy+dy[fd]
    moved+=1
    if moved == mx_move:
        if not flag: fd = (fd+1)%4
        else: fd = (fd-1)%4
        turned+=1
        moved = 0
    if turned == 2:
        if not flag: mx_move+=1
        else: mx_move-=1
        turned = 0
    
    if (fx,fy) == (0,0):
        fd = 2
        turned = -1
        moved = 0
        mx_move = N-1
        flag = True
    elif (fx,fy) == (N//2,N//2):
        fd = 0
        turned = 0
        moved = 0
        mx_move = 1
        flag = False
    
    board = [[0]*N for _ in range(N)]
    board[fx][fy] = 1

    # 술래 시야 체크
    sight = [(fx,fy), (fx+dx[fd], fy+dy[fd]), (fx+dx[fd]*2, fy+dy[fd]*2)]
    for i in range(len(hide)-1,-1,-1):
        if (hide[i][0],hide[i][1]) in sight and (hide[i][0],hide[i][1]) not in trees:
            hide.pop(i)
            dir.pop(i)
            scores+=turn
    
    if not hide: break

print(scores)