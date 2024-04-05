"""
구현
"""

"""
격자판 크기 r,c
상어 수 m

상어 정보: r,c,s,d,z
r,c: 위치
s: 속력, d: 이동방향, z: 크기
d: 1,2,3,4 (북,남,동,서)

좌표: (r,c), 1부터 시작
칸에는 상어가 최대 한마리 들어있음

낚시왕은 처음에 1번 열의 한칸 왼쪽에 있음
가장 오른쪽 열의 오른쪽 칸으로 가면 이동 멈춤

1. 낚시왕이 오른쪽으로 한 칸 이동
2. 낚시왕이 있는 열에서 땅과 가장 가까운 상어를 잡는다. 잡힌 상어는 사라짐
3. 상어가 이동

상어는 입력으로 주어진 속도로 이동, 단위는 칸/초
상어가 격자판의 경계를 넘을 경우에는 방향을 반대로 바꾸고 속력은 유지

상어가 이동을 마친 후에 한 칸에 상어가 두 마리 있을 경우,
크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹음

낚시왕이 잡은 상어 크기의 합
"""

"""
낚시꾼 이동
낚시꾼 열 탐색
상어 이동 구현
상어 잡아먹기 구현
"""

r, c, m = map(int, input().split())

# 북 - 남 - 동 - 서                                                                       
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 낚시터
graph = [[[] for _ in range(c)] for _ in range(r)]

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    graph[x - 1][y - 1].append([z, s, d - 1])


def move_shark():
    global graph
    # 이동한 뒤의 상어 상태를 저장할 배열
    board = [[[] for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if graph[i][j]:
                x, y = i, j
                z, s, d = graph[i][j][0]
                s_count = s
                while s_count > 0:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 범위 벗어나면
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        # 방향 바꿔서 다시 이동
                        if d in [0, 2]:
                            d += 1
                        elif d in [1, 3]:
                            d -= 1
                        continue
                    # 범위 안 벗어나면
                    else:
                        # 이동
                        x, y = nx, ny
                        s_count -= 1
                # 이동 끝난 상태 저장
                board[x][y].append([z, s, d])

    # 이동 끝난 상태로 갱신
    for i in range(r):
        for j in range(c):
            graph[i][j] = board[i][j]


cnt = 0

# j(열)이 증가하는 것 자체가 낚시왕이 열을 한 칸씩 이동하는 것과 같음
for j in range(c):
    for i in range(r):
        if len(graph[i][j]) > 0:
            value = graph[i][j][0]
            cnt += value[0]
            graph[i][j].remove(value)
            break
    
    # 상어 이동
    move_shark()
    
    # 겹치는 상어 제거
    for p in range(r):
        for q in range(c):
            if len(graph[p][q]) > 1:
                # 상어 무게가 내림차순이 되게 정렬
                graph[p][q].sort(reverse=True)
                # 첫번째 상어(젤 무거운 상어) 제외한 나머지 상어 pop
                while len(graph[p][q]) >= 2:
                    graph[p][q].pop()

print(cnt)