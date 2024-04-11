"""
구현
"""

"""
땅 크기: n x n
좌표: (r,c), 1부터 시작
처음에 양분은 모든 칸에 5씩
M개의 나무를 심음
x,y,z: x,y는 좌표 z는 나이

봄엔 나무가 자신의 나이만큼 양분을 먹고, 나이가 1증가
하나의 칸에 여러 개 나무가 있다면 어린 나무부터 양분을 먹는다.
자신의 나이만큼 양분을 먹을 수 없을 경우 즉시 죽음.

여름에는 봄에 죽은 나무가 양분으로 변함.
죽은 나무마다 나이를 2로 나눈 값이 양분으로 추가. (소수점 버림)

가을엔 나무 번식함.
번식하는 나무는 나이가 5의 배수여야 하고, 인접한 8개의 칸에 나이가 1인 나무가 생김.

겨울엔 땅에 양분을 추가.
각 칸에 추가되는 양분의 양은 A[r][c]

K년이 지난 후 땅에 살아있는 나무의 개수
"""

from collections import deque

n, m, k = map(int, input().split(' '))

# 양분 공급량
a = [list(map(int, input().split(' '))) for _ in range(n)]
# 양분
nutrient = [[5] * n for _ in range(n)]
# 나무 나이
trees = [[deque() for _ in range(n)] for _ in range(n)]
# 죽은 나무
dead_trees = [[list() for _ in range(n)] for _ in range(n)]

# 입력받은 초기 나무 위치, 나이 저장
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 봄, 여름
def spring_summer():
    for i in range(n):
        for j in range(n):
            len_ = len(trees[i][j]) # 현재 위치에 있는 나무 총 개수
            # 현재 위치의 나무들 탐색
            for k in range(len_):
                # 나무가 죽는 경우
                if nutrient[i][j] < trees[i][j][k]:
                    # 죽는 나무들은 따로 저장
                    for _ in range(k, len_):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break
                # 나무가 양분 먹고 성장하는 경우
                else:
                    nutrient[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
    # 죽은 나무들 만큼 양분 저장
    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                nutrient[i][j] += dead_trees[i][j].pop() // 2

# 가을, 겨울
def fall_winter():
    for i in range(n):
        for j in range(n):
            # 현재 위치의 나무들 탐색
            for k in range(len(trees[i][j])):
                # 현재 나무의 나이가 씨를 뿌릴 수 있는 상태인 경우
                if trees[i][j][k] % 5 == 0:
                    # 8방향에 씨 뿌림
                    for t in range(8):
                        nx = i + dx[t]
                        ny = j + dy[t]
                        # 범위 체크
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        # 새로 태어난 나무들 앞으로 삽입
                        trees[nx][ny].appendleft(1)
            # 밭에 양분 추가
            nutrient[i][j] += a[i][j]

for i in range(k):
    spring_summer()
    fall_winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)