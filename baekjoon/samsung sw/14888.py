"""
backtracking
"""

n = int(input())
nl = list(map(int, input().split()))
pl,mi,mu,di = map(int, input().split())

maxv = -1e9
minv = 1e9

def backtracking(i, num):
    global n,nl,pl,mi,mu,di,maxv,minv
    if i==n:
        maxv=max(maxv, num)
        minv=min(minv, num)
    else:
        if pl>0:
            pl-=1
            backtracking(i+1, num+nl[i])
            pl+=1
            #print("pl:",pl)
        if mi>0:
            mi-=1
            backtracking(i+1, num-nl[i])
            mi+=1
            #print("mi:",mi)
        if mu>0:
            mu-=1
            backtracking(i+1, num*nl[i])
            mu+=1
            #print("mu:",mu)
        if di>0:
            di-=1
            backtracking(i+1, int(num/nl[i]))
            di+=1
            #print("di:",di)

backtracking(1, nl[0])

print(maxv)
print(minv)