n = int(input())
li = [int(input()) for _ in range(n)]

prime = []
check = [1]*1000001
check[0] = 0
check[1] = 0
for i in range(2, 1000001):
    if check[i] == 1:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j]=0

for num in li:
    cnt=0
    for item in prime:
        if item>=num: break
        elif check[num-item] and item<=num-item: cnt+=1
    print(cnt)