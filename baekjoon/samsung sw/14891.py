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

from collections import deque

wheels = [deque(map(int, list(input()))) for _ in range(4)]
rights = [wheels[i][2] for i in range(len(wheels))]
lefts = [wheels[i][6] for i in range(len(wheels))]

k = int(input())
move = [tuple(map(int, input().split())) for _ in range(k)]


def rotate(num, dir):
    global wheels
    wheel = wheels[num]

    if dir == 1: # 시계방향
        last = wheel.pop()
        wheel.appendleft(last)
    else: # 반시계방향
        first = wheel.popleft()
        wheel.append(first)

    wheels[num] = wheel

for (num, dir) in move:
    rotate(num-1, dir)

    tmp = num - 1
    d = dir
    while tmp < 3:
        d *= -1
        if rights[tmp] != lefts[tmp+1]: 
            rotate(tmp+1, d)
            tmp+=1
        else: break
    
    tmp = num -1
    d = dir
    while tmp > 0:
        d *= -1
        if lefts[tmp] != rights[tmp-1]: 
            rotate(tmp-1, d)
            tmp-=1
        else: break
    
    rights = [wheels[i][2] for i in range(len(wheels))]
    lefts = [wheels[i][6] for i in range(len(wheels))]

answer = 0
val = 1
for wheel in wheels:
    answer += wheel[0]*val
    val*=2

print(answer)