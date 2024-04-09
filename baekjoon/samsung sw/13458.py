"""
N: 시험장 수
A: 각 시험장의 응시자 수
B: 총감독관 감시 가능 수
C: 부감독관 감시 가능 수
"""

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

num = [1] * N

for i in range(len(A)):
    rest = A[i] - B 
    if rest > 0:
        if rest%C == 0:
            sub = rest/C
        else:
            sub = rest//C + 1
        num[i] += int(sub)

print(sum(num))