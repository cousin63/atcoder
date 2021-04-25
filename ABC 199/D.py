n,m = map(int,input().split())
x = [[] for _ in range(n)]
ans = 1
for i in range(m):
    a,b = map(int,input().split())
    a = a-1
    b = b-1
    if b < a:
        x[a].append(b)
    if a < b:
        x[b].append(a)
#print(x)
for i in range(n):
    a = 3-len(x[i])
    if a <= 0:
        print(0)
        exit()
    else:
        ans = ans * (a)
print(ans)