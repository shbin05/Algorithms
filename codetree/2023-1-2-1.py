N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
pos = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
exit = list(map(lambda x: int(x)-1, input().split()))

dist = [0]*M



for _ in range(K):
