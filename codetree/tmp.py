"""
K명 정령
십자 모양, 4칸 중 한칸은 출구

골렘 중앙이 c열이 되도록 하는 위치에서 내려오고, 출구는 d 방향에 위치.

골렘이 최대한 남쪽으로 이동했지만 몸 일부가 숲을 벗어난 상태라면,
해당 골렘을 포함해 숲에 위치한 모든 골렘들 지우고, (최종위치 답에 포함 x)
다음 골렘부터 새롭게 시작.

1. 골렘 내려오기 구현
2. 내려오다 막히면 서쪽 이동, 동쪽 이동 차례대로 시도.
    서쪽 이동 시 출구가 반시계 방향으로 이동.
    동쪽 이동 시 출구가 시계 방향으로 이동.
3. 정령 이동 -> bfs
    출구 찾기,
    최대한 아래로 내려가기

d: 0 1 2 3 상우하좌
"""

R,C,K = map(int, input().split())
board = [[0]*C for _ in range(R+3)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for num in range(1, K+1):
    c,d = map(int, input().split())

    x,y = 1,c-1
    # 아래로 내려오기
    while True:
        if x+2 == R+3: break # 맨 아래
        elif board[x+2][y]!=0: break # 다른 골렘에 막힘
        x+=1
    if x+2 < R+3:
        move_l = False
        # 서쪽 이동
        while True:
            if 0<=x+2<R+3 and 0<=y-2<C: 
                if board[x-1][y-1] == 0 and board[x][y-2] == 0 and board[x+1][y-1] == 0:
                    if board[x+1][y-2] == 0 and board[x+2][y-1] == 0:
                        x+=1
                        y-=1
                        d = (d-1)%4
                        move_l = True
                    else: break
                else: break 
            else: break
    if x+2 < R+3 and not move_l:
        # 동쪽 이동
        while True:
            if 0<=x+2<R+3 and 0<=y+2<C:
                if board[x-1][y+1] == 0 and board[x][y+2] == 0 and board[x+1][y+1] == 0:
                    if board[x+1][y+2] == 0 and board[x+2][y+1] == 0:
                        x+=1
                        y+=1
                        d = (d+1)%4
                    else: break
                else: break    
            else: break

    if x < 4: # board 꽉 찼을 시
        board = [[0]*C for _ in range(R+3)]
    else:
        # 골렘 표시
        board[x][y] = num
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if i == d: board[nx][ny] = -num
            else: board[nx][ny] = num
    

for line in board:
    print(line)