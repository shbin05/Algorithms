N, L = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

def pos(cur):
    """
    1. 높이 차이가 1인 경우에만 경사로 설치 가능
    2. 현재 높이 < 이전 높이, 경사로 설치를 위해 오른쪽 스캔 (낮은 곳에 경사로 설치)
    3. 현재 높이 > 이전 높이, 경사로 설치를 위해 왼쪽 스캔 (낮은 곳에 경사로 설치)
    """
    for i in range(1, N):
        if abs(cur[i] - cur[i-1]) > 1: # 높이 차이가 1일 때만 가능
            return False
        if cur[i] < cur[i-1]: # 현재 < 이전, 경사로를 만들기 위해 오른쪽을 스캔 (낮은 곳에 경사로 설치)
            for j in range(L):  # l 만큼 경사로 너비 필요 
                if i + j >= N or used[i+j] or cur[i] != cur[i+j]: # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우
                    return False
                if cur[i] == cur[i+j]: # 높이가 같은 경우 사용 여부 체크 
                    used[i + j] = True
        elif cur[i] > cur[i-1]: # 현재 > 이전, 경사로를 만들기 위해 왼쪽을 스캔
            for j in range(L):
                if i - j - 1 < 0 or cur[i-1] != cur[i-j-1] or used[i-j-1]: # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우
                    return False
                if cur[i-1] == cur[i-j-1]: # 높이가 같은 경우 사용 여부 체크 
                     used[i-j-1] = True
    
    return True   

for i in range(N):
    used = [False for _ in range(N)] 
    if pos(heights[i]): 
        cnt += 1

for i in range(N):
    used = [False for _ in range(N)]
    if pos([heights[j][i] for j in range(N)]):  
        cnt += 1

print(cnt)