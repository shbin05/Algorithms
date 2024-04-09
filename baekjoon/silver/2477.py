k = int(input())

x = []
y = []
li=[]

for _ in range(6):
    l = list(map(int, input().split()))
    dir = l[0]
    len = l[1]
    
    if dir ==1:
        x.append(len)
        li.append(len)
    elif dir==2:
        x.append(len)
        li.append(len)
    elif dir==3:
        y.append(len)
        li.append(len)
    else:
        y.append(len)
        li.append(len)

bigx = max(x)
bigy = max(y)

ind = li.index(bigx)
h = abs(li[(ind+1)%6]-li[(ind-1)%6])

ind = li.index(bigy)
w = abs(li[(ind+1)%6]-li[(ind-1)%6])


    
print((bigx*bigy-w*h)*k)