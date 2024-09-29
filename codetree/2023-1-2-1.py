N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
pos = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
exit = list(map(lambda x: int(x)-1, input().split()))

dist = [0]*M
escaped = [False]*M

def rotate():

    return

    

for _ in range(K):
    for i in range(M):
        if escaped[i]: continue
        x,y = pos[i]
        min_dist = abs(exit[0]-x)+abs(exit[1]-y)
        tmp_x,tmp_y = x,y
        for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny]==0:
                    cur_dist = abs(exit[0]-nx)+abs(exit[1]-ny)
                    if cur_dist < min_dist:
                        min_dist = cur_dist
                        tmp_x,tmp_y = nx,ny
        if tmp_x!=x or tmp_y!=y: dist[i]+=1
        pos[i] = [tmp_x,tmp_y] 
        if pos[i] == exit: escaped[i] = True
    if escaped.count(False) == 0: break

print(sum(dist))
print(*exit)
    
