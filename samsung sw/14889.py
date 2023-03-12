n = int(input())
table=[list(map(int,input().split())) for _ in range(n)]
v = [False for _ in range(n)]

minv = 99999

def backtracking(num, ind):
    global minv
    if num==n//2:
        x,y=0,0
        for i in range(n):
            for j in range(n):
                if v[i] and v[j]:
                    x += table[i][j]
                elif not v[i] and not v[j]:
                    y += table[i][j]
        minv = min(minv, abs(x-y))
    else:
        for i in range(ind, n):
            if not v[i]:
                v[i]=True
                backtracking(num+1, i+1)
                v[i]=False

backtracking(0,0)
print(minv)