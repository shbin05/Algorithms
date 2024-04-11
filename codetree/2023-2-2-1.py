"""
구현
"""

"""
게임판 n x n
좌표 (r,c), 1부터 시작

게임은 M개의 턴에 걸쳐 진행,
매 턴마다 루돌프와 산타들이 한 번씩 움직임
루돌프가 한 번 움직이고 1~P번 산타까지 순서대로 움직임.
단, 기절해있거나 격자밖으로 나간 산타들은 움직일 수 없음.
거리 계산은 유클리드 거리

루돌프는 가장 가까운 산타를 향해 1칸 돌진
가장 가까운 산타가 2명 이상이면 r,c 좌표가 큰 순으로 돌진
루돌프는 상하좌우, 대각선 포함한 8방향 중 하나로 돌진

산타는 1번부터 P번까지 순서대로 움직임
산타는 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동
다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없음
움직일 수 있는 칸이 없으면 움직이지 않음.
상하좌우 4방향 중 한곳으로 이동, 가장 가까워질 수 있는 방향이 여러 개라면 상우하좌 우선순위에 맞게 움직임.

산타와 루돌프가 같은 칸에 있으면 충돌 발생
1. 루돌프가 움직여서 충돌하면 산타는 C만큼의 점수 얻고 산타는 루돌프가 이동해온 방향으로 C칸 밀려남
2. 산타가 움직여서 충돌하면 산타는 D만큼의 점수 얻고, 산타는 자신이 이동해온 반대 방향으로 D칸 밀려남
밀려나는 도중에는 충돌 발생하지 않음
밀려난 위치가 게임판 밖이면 산타는 게임에서 탈락

산타가 충돌 후 착지하게 되는 칸에 다른 산타가 있으면 그 산타는 해당 방향으로 밀려나고, 연쇄 반응 가능
게임판 밖으로 밀려난 산타는 탈락

산타가 루돌프와 충돌하면 기절하고, k번째 턴이라면 k+1번째 턴까지 기절함
기절한 산타는 움직일 수 없지만, 충돌이나 상호작용으로 밀려날 수는 있음
기절한 산타를 돌진 대상으로 선택할 수 있음

P명의 산타가 모두 게임에서 탈락하면 즉시 게임 종료
매 턴 이후 탈락하지 않은 산타들에게는 1점씩 부여
각 산타가 얻은 최종 점수를 구하기
"""

# (x, y)가 보드 내의 좌표인지 확인하는 함수입니다.
def is_inrange(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

n, m, p, c, d = map(int, input().split())
rudolf = tuple(map(int, input().split()))

points = [0 for _ in range(p + 1)]
pos = [(0, 0) for _ in range(p + 1)]
board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
is_live = [False for _ in range(p + 1)]
stun = [0 for _ in range(p + 1)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board[rudolf[0]][rudolf[1]] = -1

for _ in range(p):
    id, x, y = tuple(map(int, input().split()))
    pos[id] = (x, y)
    board[pos[id][0]][pos[id][1]] = id
    is_live[id] = True

for t in range(1, m + 1):
    closestX, closestY, closestIdx = 10000, 10000, 0

    # 살아있는 포인트 중 루돌프에 가장 가까운 산타를 찾습니다.
    for i in range(1, p + 1):
        if not is_live[i]:
            continue

        currentBest = ((closestX - rudolf[0]) ** 2 + (closestY - rudolf[1]) ** 2, (-closestX, -closestY))
        currentValue = ((pos[i][0] - rudolf[0]) ** 2 + (pos[i][1] - rudolf[1]) ** 2, (-pos[i][0], -pos[i][1]))

        if currentValue < currentBest:
            closestX, closestY = pos[i]
            closestIdx = i

    # 가장 가까운 산타의 방향으로 루돌프가 이동합니다.
    if closestIdx:
        prevRudolf = rudolf
        moveX = 0
        if closestX > rudolf[0]:
            moveX = 1
        elif closestX < rudolf[0]:
            moveX = -1

        moveY = 0
        if closestY > rudolf[1]:
            moveY = 1
        elif closestY < rudolf[1]:
            moveY = -1

        rudolf = (rudolf[0] + moveX, rudolf[1] + moveY)
        board[prevRudolf[0]][prevRudolf[1]] = 0

    # 루돌프의 이동으로 충돌한 경우, 산타를 이동시키고 처리를 합니다.
    if rudolf[0] == closestX and rudolf[1] == closestY:
        firstX = closestX + moveX * c
        firstY = closestY + moveY * c
        lastX, lastY = firstX, firstY

        stun[closestIdx] = t + 1

        # 만약 이동한 위치에 산타가 있을 경우, 연쇄적으로 이동이 일어납니다.
        while is_inrange(lastX, lastY) and board[lastX][lastY] > 0:
            lastX += moveX
            lastY += moveY

        # 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해,
        # 순차적으로 보드판에 있는 산타를 한칸씩 이동시킵니다.
        while not (lastX == firstX and lastY == firstY):
            beforeX = lastX - moveX
            beforeY = lastY - moveY

            if not is_inrange(beforeX, beforeY):
                break

            idx = board[beforeX][beforeY]

            if not is_inrange(lastX, lastY):
                is_live[idx] = False
            else:
                board[lastX][lastY] = board[beforeX][beforeY]
                pos[idx] = (lastX, lastY)

            lastX, lastY = beforeX, beforeY

        points[closestIdx] += c
        pos[closestIdx] = (firstX, firstY)
        if is_inrange(firstX, firstY):
            board[firstX][firstY] = closestIdx
        else:
            is_live[closestIdx] = False

    board[rudolf[0]][rudolf[1]] = -1;

    # 각 산타들은 루돌프와 가장 가까운 방향으로 한칸 이동합니다.
    for i in range(1, p+1):
        if not is_live[i] or stun[i] >= t:
            continue

        minDist = (pos[i][0] - rudolf[0])**2 + (pos[i][1] - rudolf[1])**2
        moveDir = -1

        for dir in range(4):
            nx = pos[i][0] + dx[dir]
            ny = pos[i][1] + dy[dir]

            if not is_inrange(nx, ny) or board[nx][ny] > 0:
                continue

            dist = (nx - rudolf[0])**2 + (ny - rudolf[1])**2
            if dist < minDist:
                minDist = dist
                moveDir = dir

        if moveDir != -1:
            nx = pos[i][0] + dx[moveDir]
            ny = pos[i][1] + dy[moveDir]

            # 산타의 이동으로 충돌한 경우, 산타를 이동시키고 처리를 합니다.
            if nx == rudolf[0] and ny == rudolf[1]:
                stun[i] = t + 1

                moveX = -dx[moveDir]
                moveY = -dy[moveDir]

                firstX = nx + moveX * d
                firstY = ny + moveY * d
                lastX, lastY = firstX, firstY

                if d == 1:
                    points[i] += d
                else:
                    # 만약 이동한 위치에 산타가 있을 경우, 연쇄적으로 이동이 일어납니다.
                    while is_inrange(lastX, lastY) and board[lastX][lastY] > 0:
                        lastX += moveX
                        lastY += moveY

                    # 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해,
                    # 순차적으로 보드판에 있는 산타를 한칸씩 이동시킵니다.
                    while lastX != firstX or lastY != firstY:
                        beforeX = lastX - moveX
                        beforeY = lastY - moveY

                        if not is_inrange(beforeX, beforeY):
                            break

                        idx = board[beforeX][beforeY]

                        if not is_inrange(lastX, lastY):
                            is_live[idx] = False
                        else:
                            board[lastX][lastY] = board[beforeX][beforeY]
                            pos[idx] = (lastX, lastY)

                        lastX, lastY = beforeX, beforeY

                    points[i] += d
                    board[pos[i][0]][pos[i][1]] = 0
                    pos[i] = (firstX, firstY)
                    if is_inrange(firstX, firstY):
                        board[firstX][firstY] = i
                    else:
                        is_live[i] = False
            else:
                board[pos[i][0]][pos[i][1]] = 0
                pos[i] = (nx, ny)
                board[nx][ny] = i

    # 라운드가 끝나고 탈락하지 않은 산타들의 점수를 1 증가시킵니다.
    for i in range(1, p+1):
        if is_live[i]:
            points[i] += 1


# 결과를 출력합니다.
for i in range(1, p + 1):
    print(points[i], end=" ")