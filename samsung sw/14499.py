"""
지도 크기: N x M
지도 좌표: (r,c)

주사위
  2
4 1 3 6
  5
지도 위에 윗 면이 1 동쪽을 바라보는 방향이 3인 상태로 놓여있음
좌표는 (x,y)

이동한 칸에 쓰여 있는 수가 0이면, 주사위 바닥면의 숫자가 칸에 복사됨
아니면, 칸에 쓰여 있는 수가 주사위 바닥면으로 복사되고, 칸의 숫자는 0으로

명령 개수: K
dir: 방향 (1:동, 2:서, 3:북, 4:남)
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M, x, y, K= map(int, input().split())
num_map = [list(map(int, input().split())) for _ in range(N)]
dir = list(map(int, input().split()))
dice = [0] * 6 # [top, left, front, right, back, bottom]


"""
  2
4 1 3 6
  5
[2, 4, 1, 3, 6, 5]

동
  4
5 1 2 6
  3
[4, 5, 1, 2, 6, 3]

서
  3
2 1 5 6
  4
[3, 2, 1, 5, 6, 4]
  
남
  6
4 2 3 5
  1 
[6, 4, 2, 3, 5, 1]

북
  1
4 5 3 2
  6
[1, 4, 5, 3, 2, 6]
"""

def north(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[2]
    new_dice[1] = dice[1] 
    new_dice[2] = dice[5]
    new_dice[3] = dice[3] 
    new_dice[4] = dice[0]
    new_dice[5] = dice[4]

    return new_dice

def south(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[4]
    new_dice[1] = dice[1]
    new_dice[2] = dice[0]
    new_dice[3] = dice[3]
    new_dice[4] = dice[5]
    new_dice[5] = dice[2]
      
    return new_dice

def west(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[3]
    new_dice[1] = dice[0]
    new_dice[2] = dice[2]
    new_dice[3] = dice[5]
    new_dice[4] = dice[4]
    new_dice[5] = dice[1]
    
    return new_dice

def east(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[1]
    new_dice[1] = dice[5]
    new_dice[2] = dice[2]
    new_dice[3] = dice[0]
    new_dice[4] = dice[4]
    new_dice[5] = dice[3]
    
    return new_dice

for d in dir:
    if d ==1: # 동쪽
        if y+1 >= M: continue
        dice = east(dice)
        y+=1
        if num_map[x][y] == 0:
            num_map[x][y] = dice[5]
            print(dice[0])
        else:
            dice[5] = num_map[x][y]
            num_map[x][y]=0
            print(dice[0])
    elif d==2: # 서쪽
        if y-1 < 0: continue
        dice = west(dice)
        y-=1
        if num_map[x][y] == 0:
            num_map[x][y] = dice[5]
            print(dice[0])
        else:
            dice[5] = num_map[x][y]
            num_map[x][y]=0
            print(dice[0])
    elif d==3: # 북쪽
        if x-1 < 0: continue
        dice = north(dice)
        x-=1
        if num_map[x][y] == 0:
            num_map[x][y] = dice[5]
            print(dice[0])
        else:
            dice[5] = num_map[x][y]
            num_map[x][y]=0
            print(dice[0])
    else: # 남쪽
        if x+1 >= N: continue
        dice = south(dice)
        x+=1
        if num_map[x][y] == 0:
            num_map[x][y] = dice[5]
            print(dice[0])
        else:
            dice[5] = num_map[x][y]
            num_map[x][y]=0
            print(dice[0])

    
