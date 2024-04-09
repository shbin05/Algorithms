"""
구현
"""

"""
크기: n x n
다섯 개의 선거구가 있고, 각 구역은 다섯 선거구 중 하나에 포함
선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 함

기준점 (x,y)와 경계의 길이 d1,d2를 정함 (1 <= x,y <= n)
1번 선거구: 1 <= r < x+d1, 1 <= c <=y
2번 선거구: 1 <= r < x+d2, y < c <= n
3번 선거구: x+d1 <= r <= n, 1 <= c < y-d1+d2
4번 선거구: x+d2 < r <= n, y-d1+d2 <= c <= n
경계선과 경계선의 안에 포함되어 있는 곳은 5번 선거구

(r,c)의 인구는 A[r-1][c-1]이고
선거구를 나누는 방법 중에서 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값

좌표 관계가 복잡한 문제는 좌표가 1부터 시작한다면, 인덱스 그대로 반영할 수 있도록 선언
"""

n = int(input())
A = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(1, n + 1) :
    total += sum(A[i])

def calculate(x, y, d1, d2) :
    division = [[0] * (n + 1) for _ in range(n + 1)]

    # 5번 선거구 먼저 선언
    division[x][y] = 5
    for i in range(1, d1 + 1) :
        division[x+i][y-i] = 5
    for i in range(1, d2 + 1) :
        division[x+i][y+i] = 5
    for i in range(1, d2 + 1) :
        division[x+d1+i][y-d1+i] = 5
    for i in range(1, d1 + 1) :
        division[x+d2+i][y+d2-i] = 5

    population = [0] * 5
    # 1번 선거구
    for r in range(1, x + d1) :
        for c in range(1, y + 1) :
            if division[r][c] == 5 :
                break
            else :
                population[0] += A[r][c]

    # 2번 선거구
    for r in range(1, x + d2 + 1) :
        for c in range(n, y, -1) :
            if division[r][c] == 5 :
                break
            else :
                population[1] += A[r][c]

    # 3번 선거구
    for r in range(x + d1, n + 1) :
        for c in range(1, y - d1 + d2) :
            if division[r][c] == 5 :
                break
            else :
                population[2] += A[r][c]

    # 4번 선거구
    for r in range(x + d2 + 1, n + 1) :
        for c in range(n, y - d1 + d2 - 1, -1) :
            if division[r][c] == 5 :
                break
            else :
                population[3] += A[r][c]

    # 5번 선거구
    population[4] = total - sum(population)
    return max(population) - min(population)

minimum = int(1e9)
for x in range(1, n + 1) :
    for y in range(1, n + 1) :
        for d1 in range(1, n + 1) :
            for d2 in range(1, n + 1) :

                if x + d1 + d2 > n :
                    continue
                if y - d1 < 1 :
                    continue
                if y + d2 > n :
                    continue

                minimum = min(minimum, calculate(x, y, d1, d2))

print(minimum)