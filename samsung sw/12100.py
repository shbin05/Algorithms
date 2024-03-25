"""
구현
list transpose
"""

import sys
from itertools import product
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def push(line, dir):
    line = [num for num in line if num != 0]
    if dir == 'Right' or dir == 'Down': line.reverse()
    for i in range(0, len(line)-1):
        if (line[i] == line[i+1]) and (line[i]!=0): 
            line[i] *= 2
            line.pop(i+1)
            line.append(0)
    while len(line) < N: line.append(0)
    
    if dir == 'Right' or dir == 'Down': 
        line.reverse()
        return line
    else: return line

max_value = 0

for i in product(['Left', 'Right', 'Up', 'Down'], repeat=5):
    order = i
    copied = deepcopy(board)
    for o in order:
        if o == 'Left':
            j=0
            for line in copied:
                copied[j] = push(line, 'Left')
                j+=1
        elif o == 'Up':
            tmp = [list(line) for line in zip(*copied)]
            j=0
            for line in tmp:
                tmp[j] = push(line, 'Up')
                j+=1
            copied = [list(line) for line in zip(*tmp)]
        elif o == 'Down':
            tmp = [list(line) for line in zip(*copied)]
            j=0
            for line in tmp:
                tmp[j] = push(line, 'Down')
                j+=1
            copied = [list(line) for line in zip(*tmp)]
        elif o == 'Right':
            j=0
            for line in copied:
                copied[j] = push(line, 'Right')
                j+=1

    for line in copied:
        tmp = max(line)
        if tmp > max_value: 
            max_value = tmp

print(max_value)