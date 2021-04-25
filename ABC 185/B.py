n,m,t = map(int,input().split())
maxn = n
bb = 0
for i in range(m):
    a,b = map(int,input().split())
    n = n-(a-bb)
    if n<=0:
        print("No")
        exit()
    else:
        n += b-a
        bb = b
        if n >= maxn:
            n = maxn
n = n-(t-b)
if n <= 0:
    print("No")
    exit()
print("Yes")