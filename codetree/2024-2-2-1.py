from collections import deque

N,M = map(int, input().split())
# 집, 공원 위치
hx,hy,px,py = map(int,input().split())
# 전사 위치
s = list(map(int, input().split()))
swords = list(zip(s[::2], s[1::2]))

# 도로 정보
road = [list(map(int, input().split())) for _ in range(N)]
# 마녀 위치 저장
board = [[0]*N for _ in range(N)]
wx,wy = hx,hy
board[wx][wy] = 1

def in_board(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    else:
        return False

def find_park(): # 공원에서부터 거꾸로 탐색: 우좌하상 우선순위
    q = deque()
    q.append((px,py))

    visited = []
    prev = [[(-1,-1) for _ in range(N)] for _ in range(N)]

    while q:
        x,y = q.popleft()
        if (x,y)==(wx,wy):
            break
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x+dx,y+dy
            if in_board(nx,ny) and road[nx][ny] == 0 and (nx,ny) not in visited:
                q.append((nx,ny))
                visited.append((nx,ny))
                prev[nx][ny]=(x,y)

    if prev[wx][wy]==(-1,-1):
        return -1
    else:
        return prev[wx][wy]

def find_swords(dx,dy):
    sight = [[0]*N for _ in range(N)]
    cnt = 0

    # 1차적으로 표시
    x,y = wx,wy
    dx2,dy2 = dy,dx
    dx3,dy3 = dy,-dx
    count = 1
    while True:
        nx,ny = x+dx*count,y+dy*count
        if in_board(nx,ny):
            sight[nx][ny]=1

            for i in range(1,count+1):
                nx2,ny2 = nx+dx2*i,ny+dy2*i
                if in_board(nx2,ny2):
                    sight[nx2][ny2]=1
                nx3,ny3 = nx+dx3*i,ny+dy3*i
                if in_board(nx3,ny3):
                    sight[nx3][ny3]=1
        else: break
        count+=1
    
    # 가려지는 전사들 제외
    for sx,sy in set(swords):
        if sight[sx][sy] == 1:
            sight[sx][sy]=2
            # 일직선 세로거나 가로
            if (dx!=0 and wx==sx) or (dy!=0 and wy==sy):
                count=1
                while True:
                    nx,ny = sx+dx*count,sy+dy*count
                    if in_board(nx,ny):
                        sight[nx][ny]=0
                    else: break
                    count+=1
            else:
                # 위
                if dx<0:
                    if sy < wy: # 왼쪽인 경우
                        dx2,dy2 = dy,dx
                    else: # 오른쪽인 경우
                        dx2,dy2 = dy,-dx
                # 아래
                elif dx>0:
                    if sy < wy: # 왼쪽인 경우
                        dx2,dy2 = dy,-dx
                    else: # 오른쪽인 경우
                        dx2,dy2 = dy,dx
                # 오른
                elif dy>0:
                    if sx > wx: # 위쪽인 경우
                        dx2,dy2 = dy,-dx
                    else: # 아래쪽인 경우
                        dx2,dy2 = dy, dx
                # 왼
                else:
                    if sx > wx: # 위쪽인 경우
                        dx2,dy2 = dy,dx
                    else: # 아래쪽인 경우
                        dx2,dy2 = dy,-dx
                
                count = 1
                while True:
                    nx,ny = sx+dx*count,sy+dy*count
                    if in_board(nx,ny):
                        sight[nx][ny]=0

                        for i in range(1,count+1):
                            nx2,ny2 = nx+dx2*i,ny+dy2*i
                            if in_board(nx2,ny2):
                                sight[nx2][ny2]=0
                    else: break
                    count+=1

    return sight

while (wx,wy)!=(px,py):
    # 마녀 이동
    next = find_park()
    if next == -1:
        print(-1)
        break
    else:
        nwx,nwy = next
        board[wx][wy] = 0
        wx,wy = nwx,nwy
        board[nwx][nwy] = 1

    if (wx,wy)==(px,py):
        print(0)
        break

    # 메두사 시선
    sight = [[0]*N for _ in range(N)]
    seen = 0
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]: # 상하좌우 순서대로
        t_sight = find_swords(dx,dy)
        cnt = 0
        for line in t_sight:
            cnt+=line.count(2)
        if cnt > seen:
            seen = cnt
            sight = t_sight
    
    stunned = [False]*len(swords)
    for i,(sx,sy) in enumerate(swords):
        if sight[sx][sy]==2:
            stunned[i]=True

    # 전사 이동
    moved_sum=0
    for i,(sx,sy) in enumerate(swords):
        if stunned[i]: continue
        # 첫 이동
        dist = abs(wx-sx)+abs(wy-sy)
        ndx,ndy = 0,0
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]: #상하좌우
            nx,ny = sx+dx,sy+dy
            if in_board(nx,ny) and sight[nx][ny]==0:
                ndist = abs(wx-nx)+abs(wy-ny)
                if ndist < dist:
                    dist = ndist
                    ndx,ndy = dx,dy
        # 이동했을 경우
        if (ndx,ndy)!=(0,0):
            moved_sum+=1
            sx,sy = sx+ndx,sy+ndy
            swords[i]=sx,sy
            # 메두사 만나지 않았을 경우 
            if (sx,sy)!=(wx,wy):
                # 두번째 이동
                dist = abs(wx-sx)+abs(wy-sy)
                ndx,ndy = 0,0
                for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]: #좌우상하
                    nx,ny = sx+dx,sy+dy
                    if in_board(nx,ny) and sight[nx][ny]==0:
                        ndist = abs(wx-nx)+abs(wy-ny)
                        if ndist < dist:
                            dist = ndist
                            ndx,ndy = dx,dy
                # 이동했을 경우
                if (ndx,ndy)!=(0,0):
                    moved_sum+=1
                    sx,sy = sx+ndx,sy+ndy
                    swords[i]=sx,sy

    # 이번 턴 메두사 만난 전사 수
    attacked = swords.count((wx,wy))

    # 메두사 만난 전사 제거
    for i in range(attacked):
        swords.remove((wx,wy))
    
    print(moved_sum, seen, attacked)