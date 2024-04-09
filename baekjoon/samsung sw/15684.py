"""
dfs
"""

"""
N: 세로선 갯수
M: (문제에서 주어진) 가로선 갯수
H: 세로선마다 가로선을 놓을 수 있는 위치의 갯수

a,b: b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결

가장 위에 있는 점선이 1번
가장 왼쪽에 있는 세로선이 1번
"""


import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
board = [[False] * n for _ in range(h)]

for _ in range(m):
    a,b = map(int, input().split())
    board[a-1][b-1] = True

def check(): # i번째 세로선이 i번으로 가는지 확인
    for start in range(n): # 모든 세로선에 대해서
        now = start
        for j in range(h):
            if board[j][now] == True: now+=1 # 가로선이 오른쪽에 있는 경우
            elif now > 0 and board[j][now-1] == True: now-=1 # 가로선이 왼쪽에 있는 경우
        if now != start: return False
    return True

def dfs(cnt, x, y):
    global ans
    
    if check(): 
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt: return # 횟수가 3이거나 최솟값을 넘은 경우 바로 종료

    for i in range(x, h): # 행 탐색
        if i == x: now = y # 행 변경 전엔 지금 열부터
        else: now = 0 # 행 바뀌면 처음 열부터

        for j in range(now, n-1): # 열 탐색
            if board[i][j] == False and board[i][j+1] == False: # 오른쪽에 가로선이 없는 경우
                if j > 0 and board[i][j-1]: continue # 연달아서 놓을 수 없으므로 왼쪽에 이미 가로선 있으면 통과
                board[i][j] = True
                dfs(cnt+1, i, j+2) # 이미 탐색한 것은 건너뛰기 위함
                board[i][j] = False


ans = 4
dfs(0, 0, 0)
print(ans if ans < 4 else -1)

