"""
도시 크기: n x n
좌표: r,c (1부터 시작)
치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
거리: abs(r1-r2) + abs(c1-c2)
0: 빈칸
1: 집
2: 치킨집

최대 M개만을 남겨두고 나머지는 폐업시키되, 치킨거리가 가장 작게 되도록
"""

from collections import deque
from itertools import combinations

n, m = map(int, input().split())

house = []
chicken = []

city = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 1: house.append((i,j))
        if line[j] == 2: chicken.append((i,j))

result = float("inf")
for c in combinations(chicken, m):
    total = 0
    for h in house:
        dist = float("inf")
        for i in range(m):
            dist = min(dist, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
        total += dist
    result = min(result, total)

print(result)