"""
구현
"""

"""
방의 크기: N x M
청소기의 초기 좌표: (r,c)
d: 방향 (0,1,2,3: 북,동,남,서)
map: 0이면 청소 안한 빈칸, 1이면 벽, 2면 청소 완료된 빈칸
"""

N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = []
num = 0

for _ in range(N):
    room.append(list(map(int, input().split())))

def able(r,c):
    # 북,동,남,서 방향으로 이동 가능하고 청소 안한 빈 칸인지 여부의 list
    # 0: 이동 불가
    # 1: 이동만 가능
    # 2: 청소 가능
    li = [0,0,0,0] 

    if room[r+1][c] == 0: li[2] = 2 # 남쪽 청소 가능
    elif room[r+1][c] == 2: li[2] = 1 # 남쪽 이동 가능
    else: li[2] = 0 # 남쪽 이동 및 청소 불가

    if room[r-1][c] == 0: li[0] = 2 # 북쪽 청소 가능
    elif room[r-1][c] == 2: li[0] = 1 # 북쪽 이동 가능
    else: li[0] = 0 # 북쪽 이동 및 청소 불가

    if room[r][c+1] == 0: li[1] = 2 # 동쪽 청소 가능
    elif room[r][c+1] == 2: li[1] = 1 # 동쪽 이동 가능
    else: li[1] = 0 # 동쪽 이동 및 청소 불가

    if room[r][c-1] == 0: li[3] = 2 # 서쪽 청소 가능
    elif room[r][c-1] == 2: li[3] = 1 # 서쪽 이동 가능
    else: li[3] = 0 # 서쪽 이동 및 청소 불가

    return li

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        num += 1
    else:
        li = able(r,c)
        if d==0: # 현재 북쪽 방향일 때
            if 2 not in li: # 주변 4칸에 청소 가능한 빈칸이 없을 경우
                if li[2] == 0: break # 남쪽 이동 가능한지 확인
                else: r+=1
            else: 
                if li[3] == 2: # 서쪽 칸이 청소 가능한지 확인
                    d=3 # 방향 서쪽으로
                    c-=1
                else: d=3
        elif d==1: # 현재 동쪽 방향일 떄
            if 2 not in li: # 주변 4칸에 청소 가능한 빈칸이 없을 경우
                if li[3] == 0: break # 서쪽 이동 가능한지 확인
                else: c-=1
            else: 
                if li[0] == 2: # 북쪽 칸이 청소 가능한지 확인
                    d=0 # 방향 북쪽으로
                    r-=1
                else: d=0
        elif d==2: # 현재 남쪽 방향일 때
            if 2 not in li: # 주변 4칸에 청소 가능한 빈칸이 없을 경우
                if li[0] == 0: break # 북쪽 이동 가능한지 확인
                else: r-=1
            else:
                if li[1] == 2: # 동쪽 칸이 청소 가능한지 확인
                    d=1 # 방향 동쪽으로
                    c+=1
                else: d=1
        else: # 현재 서쪽 방향일 떄
            if 2 not in li: # 주변 4칸에 청소 가능한 빈칸이 없을 경우
                if li[1] == 0: break # 동쪽 이동 가능한지 확인
                else: c+=1
            else:
                if li[2] == 2: # 남쪽 칸이 청소 가능한지 확인
                    d=2 # 방향 남쪽으로
                    r+=1
                else: d=2

print(num)

                    
            



    
