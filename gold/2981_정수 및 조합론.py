import math

n = int(input())
li = [int(input()) for _ in range(n)]

li.sort()
diff=[]
for i in range(1, n):
    diff.append(li[i]-li[i-1])

g = diff[0]
for i in range(1, len(diff)):
    g = math.gcd(g, diff[i])

ans=[]
for i in range(2, int(math.sqrt(g))+1):
    if g%i==0:
        ans.append(i)
        ans.append(g//i)
ans.append(g)

ans = list(set(ans))
ans.sort()
print(*ans)