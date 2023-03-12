def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

n = int(input())
li = [int(input()) for i in range(n)]
diff = []

for i in range(1, len(li)):
    diff.append(li[i]-li[i-1])

v = gcd(diff[0], diff[1])
for i in range(2, len(diff)):
    v = gcd(v, diff[i])

sum = 0
for item in diff:
    sum += item//v - 1

print(sum)