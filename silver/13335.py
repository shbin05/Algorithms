"""
n: 트럭 개수
w: 동시에 올라갈 수 있는 트럭 수
l: 다리의 최대하중
a: 트럭의 무게 list
"""

n, w, l = list(map(int, input().split()))
a = list(map(int, input().split()))

time = 0
bridge = [0 for _ in range(w)]

while True:
    bridge.pop(0)
    if a:
        cur = a[0]
        if sum(bridge)+cur <= l:
            a.pop(0)
            bridge.append(cur)
        else: bridge.append(0)
    time+=1
    if not bridge:
        break

print(time)
