a,b = map(int,input().split())
alist = []
blist = []

if a>b:
    for i in range(a):
        alist.append(i+1)
    for i in range(b-1):
        blist.append(-(i+1))
    blist.append(-(sum(alist)+sum(blist)))
if b>a:
    for i in range(b):
        blist.append(-(i+1))
    for i in range(a-1):
        alist.append(i+1)
    alist.append((-(sum(blist))-sum(alist)))
if a==b:
    for i in range(b):
        blist.append(-(i+1))
    for i in range(a):
        alist.append(i+1)
print(*alist,*blist)