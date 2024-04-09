"""
구현
"""

"""
체스판 크기: n x n
사용하는 말 개수: k개

한 말이 이동할 때 위에 올려져 있는 말도 함께 이동
턴이 징행되던 중에 말이 4개 이상 쌓이면 게임 종료

A번 말이 이동하려는 칸이
1. 흰색인 경우
    이동하려는 칸에 말이 있으면 가장 위에 올려놓음.
    A,B,C 이동
    D,E -> D,E,A,B,C
2. 빨간색인 경우
    이동 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로.
    A,D,F,G 이동
    E,C,B -> E,C,B,G,F,D,A
3. 파란색인 경우
    A의 이동 방향을 반대로 하고 한 칸 이동.
    방향을 반대로 바꾼 후에 이동하려는 칸이 파란색이면 이동하지 않고 가만히 있음.
4. 체스판 벗어나는 경우 파란색과 동일하게. 

체스판 정보 
0: 흰색
1: 빨간색
2: 파란색

이동방향
1: 동
2: 서
3: 북
4: 남

게임이 종료되는 턴의 번호.
1000보다 크거나 절대로 게임이 종료되지 않는 경우 -1
"""

n,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] # 체스판 색깔 정보 저장

piece = [] # 체스말 정보 저장
state = [[[] for _ in range(n)] for _ in range(n)] # 각 칸마다 상태 저장
for i in range(k):
    r, c, d = map(int, input().split())
    piece.append([r-1, c-1, d-1])
    state[r-1][c-1].append(i)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

turn = 0
def solve(p):
    x, y, d = piece[p]
    nx = x + dx[d]
    ny = y + dy[d]

    if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2: # 체스판 밖이거나 색이 파란색일 때
        if d in [0,2]: d+=1
        elif d in [1,3]: d-=1

        # 위치, 방향 업데이트
        piece[p][2] = d
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2: # 다시 한번 체스판 밖이거나 색이 파란색일 때
            return True
    
    pieces = []
    for idx, num in enumerate(state[x][y]):
        if num == p:
            pieces.extend(state[x][y][idx:]) # 위에 있는 말들 저장
            state[x][y] = state[x][y][:idx]
            break
    
    if board[nx][ny] == 1: # 빨간색일 때
        pieces = pieces[::-1] # 뒤집기
    
    for i in pieces:
        piece[i][0], piece[i][1] = nx, ny # 말 이동
        state[nx][ny].append(i) # 말 쌓아 올리기
    
    if len(state[nx][ny]) >= 4: return False

    return True

while True:
    flag = False
    if turn > 1000:
        print(-1)
        break
    for i in range(k):
        if solve(i) == False:
            flag = True
            break
    turn+=1
    if flag == True:
        print(turn)
        break
