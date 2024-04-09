n, m, h = map(int, input().split())
board = [[False for _ in range(n)] for _ in range(h)]

for _ in range(m):
    a,b = map(int, input().split())
    board[a-1][b-1] = True

minimum = 4

def check():
    for i in range(n):
        cur = i
        for j in range(h):
            if board[j][cur]==True: cur+=1
            elif cur > 0 and board[j][cur-1] == True: cur-=1
        if cur != i: return False
    return True

def dfs(cnt, x, y):
    global minimum
    if cnt==4: return
    if check(): 
        minimum = min(cnt, minimum)
        return
    elif cnt >= minimum: return

    for i in range(x, h):
        if i == x: now = y
        else: now = 0
        for j in range(now, n-1):
            if board[i][j] == False and board[i][j+1] == False:
                if j > 0 and board[i][j-1] == True: continue
                board[i][j] = True
                dfs(cnt+1, i, j+2)
                board[i][j] = False

dfs(0, 0, 0)
print(minimum if minimum < 4 else -1)
    
            
