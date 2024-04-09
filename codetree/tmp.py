"""
구현
"""

"""
게임판 n x n
좌표 (r,c), 1부터 시작

게임은 M개의 턴에 걸쳐 진행,
매 턴마다 루돌프와 산타들이 한 번씩 움직임
루돌프가 한 번 움직이고 1~P번 산타까지 순서대로 움직임.
단, 기절해있거나 격자밖으로 나간 산타들은 움직일 수 없음.
거리 계산은 유클리드 거리

루돌프는 가장 가까운 산타를 향해 1칸 돌진
가장 가까운 산타가 2명 이상이면 r,c 좌표가 큰 순으로 돌진
루돌프는 상하좌우, 대각선 포함한 8방향 중 하나로 돌진

산타는 1번부터 P번까지 순서대로 움직임
산타는 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동
다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없음
움직일 수 있는 칸이 없으면 움직이지 않음.
상하좌우 4방향 중 한곳으로 이동, 가장 가까워질 수 있는 방향이 여러 개라면 상우하좌 우선순위에 맞게 움직임.

산타와 루돌프가 같은 칸에 있으면 충돌 발생
1. 루돌프가 움직여서 충돌하면 산타는 C만큼의 점수 얻고 산타는 루돌프가 이동해온 방향으로 C칸 밀려남
2. 산타가 움직여서 충돌하면 산타는 D만큼의 점수 얻고, 산타는 자신이 이동해온 반대 방향으로 D칸 밀려남
밀려나는 도중에는 충돌 발생하지 않음
밀려난 위치가 게임판 밖이면 산타는 게임에서 탈락

산타가 충돌 후 착지하게 되는 칸에 다른 산타가 있으면 그 산타는 해당 방향으로 밀려나고, 연쇄 반응 가능
게임판 밖으로 밀려난 산타는 탈락

산타가 루돌프와 충돌하면 기절하고, k번째 턴이라면 k+1번째 턴까지 기절함
기절한 산타는 움직일 수 없지만, 충돌이나 상호작용으로 밀려날 수는 있음
기절한 산타를 돌진 대상으로 선택할 수 있음

P명의 산타가 모두 게임에서 탈락하면 즉시 게임 종료
매 턴 이후 탈락하지 않은 산타들에게는 1점씩 부여
각 산타가 얻은 최종 점수를 구하기
"""

from collections import deque

n, m, p, c, d = map(int, input().split())
deer_x, deer_y = map(int, input().split())
deer_x -= 1
deer_y -= 1

santa = [[] for _ in range(p)]
points = [0] * p
for _ in range(p):
    i,x,y = map(int, input().split())
    santa[i-1] = [x-1,y-1]

# 1은 루돌프, 2는 산타
board = [[0]*n for _ in range(n)]
board[deer_x][deer_y] = 1
for x, y in santa:
    board[x][y] = 2

# 상우하좌, 대각선
dx = [-1, 0, 1, 0, -1, 1, 1, -1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

for _ in range(m):
    # 사슴 먼저 이동
    board[deer_x][deer_y] = 0
    minimum = int(1e9)
    candidate = [] # 거리가 가장 가까운 산타들 저장
    for i in range(len(santa)):
        x,y = santa[i]
        dist = (deer_x-x)**2 + (deer_y-y)**2
        if dist <= minimum: 
            minimum = dist
            candidate.append((x,y,dist))
    candidate.sort(key=lambda x: (x[2], -x[0], -x[1]))
    cand_x, cand_y = candidate[0][0], candidate[0][1] # 거리가 가장 가까운 산타의 x,y 좌표
    
    tmp_x, tmp_y = deer_x, deer_y
    minimum = int(1e9) 
    for i in range(8):
        nx = deer_x + dx[i]
        ny = deer_y = dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            dist = (cand_x-nx)**2 + (cand_y-ny)**2 
            if dist < minimum:
                minimum = dist
                tmp_x, tmp_y = nx, ny
            
    # 사슴 위치 업데이트
    deer_x, deer_y = tmp_x, tmp_y 
    board[deer_x][deer_y] = 1
    
    # 산타 이동
    for i in range(len(santa)):
        x,y = santa[i][0], santa[i][1]
        board[x][y] = 0
        
        tmp_x, tmp_y = x,y
        minimum = int(1e9)
        for j in range(4,-1,-1):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
                dist = (cand_x-nx)**2 + (cand_y-ny)**2 
                if dist <= minimum:
                    minimum = dist
                    tmp_x, tmp_y = nx, ny
                    
        santa[i][0], santa[i][1] = tmp_x, tmp_y
        board[tmp_x][tmp_y] = 2
    