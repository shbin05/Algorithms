"""
n: 보드 크기
k: 사과 개수
pos: 사과 위치
뱀은 처음에 맨 위 맨 좌측에 위치하고, 이 위치에는 사과가 없음
뱀의 처음 길이는 1이고 오른쪽을 향함
뱀은 매초마다 이동

l: 뱀의 방향 변환 횟수
dir: 방향 변환 정보 (X,C) => X초 뒤에 L이면 왼쪽, D면 오른쪽

1. 먼저 머리를 다음칸에 위치
2. 벽이나 자기자신과 부딪히면 게임이 끝남
3-1. 사과가 있으면 그 칸의 사과가 없어지고 꼬리는 움직이지 않음
3-2. 사과가 없으면 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌
"""

from collections import deque

n = int(input())
k = int(input())
pos = [tuple(map(int, input().split())) for _ in range(k)]
l = int(input())
change = [input().split() for _ in range(l)]
change = [[int(change[i][0]), change[i][1]] for i in range(l)]

time = 0
dir = 'E'
r,c = 0,0
snake = deque()
snake.append((r,c))

while True:
    time+=1
    if len(change)>0:
        t = change[0][0]
        if time == t+1:
            d = change[0][1]
            # L이면 왼쪽, D면 오른쪽
            if d == 'L':
                if dir == 'E': dir = 'N'
                elif dir == 'W': dir = 'S'
                elif dir == 'N': dir = 'W'
                elif dir == 'S': dir = 'E'
            else:
                if dir == 'E': dir = 'S'
                elif dir == 'W': dir = 'N'
                elif dir == 'N': dir = 'E'
                elif dir == 'S': dir = 'W'
            change.pop(0)
    
    if dir == 'E': c+=1
    elif dir == 'W': c-=1
    elif dir == 'N': r-=1
    elif dir == 'S': r+=1

    if r >= n or r < 0 or c >= n or c < 0: break
    elif (r,c) in snake: break

    if (r+1,c+1) in pos: 
        snake.append((r,c))
        pos.remove((r+1,c+1))
    else:
        snake.append((r,c))
        snake.popleft()

print(time)

