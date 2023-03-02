import sys
input = sys.stdin.readline
table = [[[0]*21 for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    if a<=0 or b<=0 or c<=0: 
        return 1
    elif a>20 or b>20 or c>20:
        return w(20,20,20)
    if table[a][b][c]: return table[a][b][c]
    if a<b and b<c:
        table[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c) 
        return table[a][b][c]
    else:
        table[a][b][c] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return table[a][b][c]

while True:
    a,b,c = map(int, input().split())
    if (a,b,c)==(-1,-1,-1): break
    else:
        val = w(a,b,c)
        print(f"w({a}, {b}, {c}) = {val}")


