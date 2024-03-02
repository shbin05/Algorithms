import itertools

n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

li = []
for _ in range(add): li.append('+')
for _ in range(sub): li.append('-')
for _ in range(mul): li.append('*')
for _ in range(div): li.append('/')

per = list(itertools.permutations(li, len(li)))

max = -float("inf")
min = float("inf")

for item in per:
    val = a[0]
    for i in range(len(item)):
        if item[i] == '+':
            val += a[i+1]
        elif item[i] == '-':
            val -= a[i+1]
        elif item[i] == '*':
            val *= a[i+1]
        else:
            val = int(val/a[i+1])
    if val > max: max = val
    if val < min: min = val

print(max)
print(min)