N,M,K = map(int, input().split())

guns = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] > 0: guns[i][j].append(line[j])

players = [[-1,-1,-1,-1]]
points = [0 for _ in range(M+1)]
board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(1, M+1):
    x,y,d,s = map(int, input().split())
    x,y = x-1,y-1
    players.append([x,y,d,s,0])
    board[x][y].append(i)

dir = [(-1,0),(0,1),(1,0),(0,-1)]

def in_board(x,y):
    if 0<=x<N and 0<=y<N: return True
    else: return False

for _ in range(K):
    # 첫번째 플레이어부터 순차적으로 이동
    for i in range(1,M+1):
        x,y,d,s,g = players[i]
        dx,dy = dir[d]

        # 방향 설정
        nx,ny = x+dx,y+dy
        if not in_board(nx,ny):
            d = (d+2)%4
            dx,dy = dir[d]
            nx,ny = x+dx,y+dy
        
        # 위치 업데이트
        board[x][y].remove(i)
        board[nx][ny].append(i)

        # 플레이어 정보 업데이트
        players[i][:3] = [nx,ny,d]

        # 이동한 칸에 플레이어 없는 경우
        x,y = nx,ny
        if len(board[x][y]) == 1:
            # 총이 있을 경우 획득
            if len(guns[x][y]) > 0: 
                if g > 0: guns[x][y].append(g)
                g = max(guns[x][y])
                guns[x][y].remove(g)
                players[i][4] = g
        
        # 이동한 칸에 플레이어가 있는 경우
        elif len(board[x][y]) == 2:
            p1 = board[x][y][0]
            p2 = board[x][y][1]

            s1 = players[p1][3]
            s2 = players[p2][3]

            g1 = players[p1][4]
            g2 = players[p2][4]

            a1 = s1 + g1
            a2 = s2 + g2

            # 승패자 결정
            if a1 > a2:
                winner = p1
                loser = p2
            elif a1 < a2:
                winner = p2
                loser = p1
            else:
                if s1 > s2:
                    winner = p1
                    loser = p2
                else:
                    winner = p2
                    loser = p1
            
            # 승자 포인트 추가
            points[winner] += abs(a1-a2)

            # 패자 총 내려놓음
            lx,ly = x,y
            if players[loser][4] > 0:
                guns[lx][ly].append(players[loser][4])
                players[loser][4] = 0
            # 패자 방향 전환 및 이동
            ld = players[loser][2]
            dx,dy = dir[ld]
            nlx,nly = lx+dx,ly+dy
            # cnt = 1
            while not in_board(nlx,nly) or len(board[nlx][nly]) > 0:
                # if cnt == 4: break
                ld = (ld+1)%4
                dx,dy = dir[ld]
                nlx,nly = lx+dx,ly+dy
                # cnt+=1
            # 패자 위치 업데이트
            board[lx][ly].remove(loser)
            board[nlx][nly].append(loser)
            # 패자 정보 업데이트
            players[loser][:3] = [nlx,nly,ld]
            # 패자 새로운 칸에서 총 있으면 줍기
            if len(guns[nlx][nly]) > 0: 
                if players[loser][4] > 0: guns[nlx][nly].append(players[loser][4])
                lg = max(guns[nlx][nly])
                guns[nlx][nly].remove(lg)
                players[loser][4] = lg
            
            # 승자 총 획득
            if len(guns[x][y]) > 0:
                if players[winner][4] > 0: guns[x][y].append(players[winner][4])
                wg = max(guns[x][y])
                guns[x][y].remove(wg)
                players[winner][4] = wg
        
        else: print("error")

print(*points[1:])
                