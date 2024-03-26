"""
구현
"""

"""
톱니바퀴 4개, 톱니 8개
N극은 0, S극은 1
K: 회전 횟수 => (톱니바퀴 번호, 방향), 1: 시계방향, -1: 반시계방향

12시 방향 index: 0
3시 방향 index: 2
9시 방향 index: 6

시계방향이면 마지막 index가 첫 index로,
반시계방향이면 첫 index가 마지막 index로

1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
"""

first = list(map(int, list(input())))
second = list(map(int, list(input())))
third = list(map(int, list(input())))
fourth = list(map(int, list(input())))

k = int(input())
move = [tuple(map(int, input().split())) for _ in range(k)]

for item in move:
 