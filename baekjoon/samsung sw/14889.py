"""
backtracking
"""

n = int(input())
table=[list(map(int,input().split())) for _ in range(n)]
visited = [False for _ in range(n)]

minv = 99999

def backtracking(num, idx):
    global minv
    if num==n//2:
        x,y=0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    x += table[i][j]
                elif not visited[i] and not visited[j]:
                    y += table[i][j]
        minv = min(minv, abs(x-y))
    else:
        for i in range(idx, n):
            if not visited[i]:
                visited[i]=True
                backtracking(num+1, i+1)
                visited[i]=False

backtracking(0,0)
print(minv)