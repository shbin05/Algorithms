"""
격자 크기 n x m, 모든 위치에 포탑 존재
각 포탑에 공격력이 존재하고, 공격력이 0이하가 되면 해당 포탑은 부서짐.

하나의 턴은 4가지 액션을 순서대로 수행하며, 총 k번 반복.
단, 부서지지 않은 포탑이 1개가 되면 즉시 중지.


1. 공격자 선정
    부서지지 않은 포탑 중 가장 약한 포탑이 공격자로 선정
    N+M 만큼 공격력 증가
    가장 약한 포탑 기준:
        1. 공격력 가장 낮은 포탑
        2. 가장 최근에 공격한 포탑 (모든 포탑은 시점 0에 공격한 경험이 있다고 가정)
        3. 포탑 위치의 행과 열의 합이 가장 큰 포탑
        4. 열 값이 가장 큰 포탑

2. 공격자의 공격
    공격자는 자신을 제외한 가장 강한 포탑 공격
    가장 강한 포탑 기준:
        1. 공격력 가장 높은 포탑
        2. 공격한지 가장 오래된 포탑
        3. 행과 열의 합이 가장 작은 포탑
        4. 열 값이 가장 작은 포탑
    공격 시 레이저 공격 먼저 시도, 안된다면 포탄 공격
    2-1. 레이저 공격 규칙
        1. 상하좌우 4개 방향으로 움직임
        2. 부서진 포탑이 있는 곳은 지날 수 없음
        3. 가장자리에서 막힌 방향으로 진행하고자 하면, 반대편으로 나옴
        공격자의 위치에서 공격 대상 포탑까지의 최단 경로로 공격함.
        최단 경로가 존재하지 않으면 포탄 공격 진행하고, 최단 경로가 2개 이상이면 우,하,좌,상 우선순위
        공격 대상은 공격자의 공격력만큼 피해를 입으며, 피해 수치만큼 공격력 줄어듦.
        레이저 경로에 있는 포탑도 공격자의 공격력의 절반만큼 공격을 받음.(소수점 버림)
    2-2. 포탄 공격 규칙
        공격 대상은 공격자의 공격력만큼 피해를 입고, 주위 8개 포탑도 절반만큼 피해를 입음. (소수점 버림)
        공격자는 해당 공격에 영향을 받지 않고, 가장자리에 포탄이 떨어지면 레이저 이동처럼 포탄의 추가 피해가 반대편 격자로.

3. 포탑 부서짐
    공격력이 0 이하가 된 포탑은 부서짐

4. 포탑 정비
    부서지지 않은 포탑 중 공격과 무관했던 포탑(공격자와 피공격자를 제외)의 공격력 1씩 증가. 
"""

from collections import deque

n,m,k = map(int, input().split())
board = [[0]*(m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
attack = [[0]*(m+1) for _ in range(n+1)]

def select_attacker():
    global board

    minimum = int(1e9)
    cand1 = [] # 공격력 가장 낮은 후보
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] <= minimum and board[i][j] > 0:
                if board[i][j] < minimum: 
                    cand1.clear()
                    minimum = board[i][j]
                cand1.append((i,j))

    if len(cand1) > 1:
        maximum = 0
        cand2 = [] # 가장 최근에 공격한 포탑 후보
        for r,c in cand1:
            if attack[r][c] >= maximum:
                if attack[r][c] > maximum:
                    cand2.clear()
                    maximum = attack[r][c]
                cand2.append((r,c))
        
        if len(cand2) > 1:
            maximum = 0
            cand3 = [] # 행과 열의 합이 큰 후보
            for r,c in cand2:
                if (r + c) >= maximum:
                    if (r + c) > maximum:
                        cand3.clear()
                        maximum = (r + c)
                    cand3.append((r,c))
            if len(cand3) > 1:
                cand3.sort(key = lambda x: -x[1])
                return cand3[0][0],cand3[0][1]
            
            else: return cand3[0][0],cand3[0][1]
        
        else: return cand2[0][0],cand2[0][1]

    else: return cand1[0][0],cand1[0][1]

def select_attacked():
    global board

    maximum = 1
    cand1 = [] # 공격력 가장 높은 후보
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] >= maximum:
                if board[i][j] > maximum:
                    cand1.clear()
                    maximum = board[i][j]
                cand1.append((i,j))
    
    if len(cand1) > 1:
        minimum = int(1e9)
        cand2 = [] # 공격한지 가장 오래된 포탑 후보
        for r,c in cand1:
            if attack[r][c] <= minimum:
                if attack[r][c] < minimum:
                    cand2.clear()
                    minimum = attack[r][c]
                cand2.append((r,c))
        
        if len(cand2) > 1:
            minimum = int(1e9)
            cand3 = [] # 행과 열의 합이 작은 후보
            for r,c in cand2:
                if (r + c) <= minimum:
                    if (r + c) < minimum: 
                        cand3.clear()
                        minimum = (r + c)
                    cand3.append((r,c))
            
            if len(cand3) > 1:
                cand3.sort(key = lambda x: x[1])
                return cand3[0][0],cand3[0][1]

            else: return cand3[0][0],cand3[0][1]
        
        else: return cand2[0][0],cand2[0][1]
    
    else: return cand1[0][0],cand1[0][1]

def try_razer(r1, c1, r2, c2):
    global board

    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    q.append((r1,c1))

    visited = [[False]*(m+1) for _ in range(n+1)]
    visited[r1][c1] = True

    prev = [[(-1,-1)]*(m+1) for _ in range(n+1)]

    flag = False
    while q:
        x,y = q.popleft()
        if x == r2 and y == c2: flag = True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx > n: nx %= n
            if ny > m: ny %= m
            if nx == 0: nx = n
            if ny == 0: ny = m
            if board[nx][ny] > 0 and not visited[nx][ny]:
                q.append((nx,ny))
                prev[nx][ny] = (x,y)
                visited[nx][ny] = True

    if flag: 
        path = deque()
        x,y = r2,c2
        while True:
            x,y = prev[x][y]
            if x == r1 and y == c1: break
            path.appendleft((x,y))
        if len(path) == 0: return "direct"
        return path
    
    return False 

def attacking(r1, c1, r2, c2):
    global board

    related = [(r1, c1), (r2, c2)]
    path = try_razer(r1, c1, r2, c2)
    if path: # 레이저 공격 가능할 시
        print("razer")
        power = board[r1][c1] + n + m
        board[r1][c1] = power
        board[r2][c2] = board[r2][c2] - power if board[r2][c2] > power else 0 # 직접 타격

        if path!="direct":
            power //= 2
            while path: # 공격 경로에 절반만큼 피해 입히기
                x,y = path.pop()
                board[x][y] = board[x][y] - power if board[x][y] > power else 0
                related.append((x,y))
    
    else: # 포탄 공격
        print("bomb")
        power = board[r1][c1] + n + m
        board[r1][c1] = power
        board[r2][c2] = board[r2][c2] - power if board[r2][c2] > power else 0 # 직접 타격
        
        dx = [-1, 0, 1, 0, 1, -1, -1, 1]
        dy = [0, 1, 0, -1, 1, 1, -1, -1]
        power //= 2
        for i in range(8):
            nx = r2+dx[i]
            ny = c2+dy[i]

            if nx > n: nx %= n
            if ny > m: ny %= m
            if nx == 0: nx = n
            if ny == 0: ny = m
            
            if nx!= r1 and ny != c1:
                board[nx][ny] = board[nx][ny] - power if board[nx][ny] > power else 0
                related.append((nx,ny))

    return related

for turn in range(1, k+1):
    attacker_r, attacker_c = select_attacker()
    attack[attacker_r][attacker_c] = turn

    attacked_r, attacked_c = select_attacked()
    related = attacking(attacker_r, attacker_c, attacked_r, attacked_c)

    cnt = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] > 0:
                cnt += 1
                if (i,j) not in related:
                    board[i][j] += 1
    
    for i in range(1, n+1):
        print(board[i][1:m+1])

    if cnt <= 1: break

maximum = 0
for i in range(1, n+1):
    maximum = max(maximum, max(board[i][1:m+1]))
print(maximum)