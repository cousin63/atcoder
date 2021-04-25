import itertools
n,m = map(int,input().split())
cond = [tuple(map(int, input().split())) for i in range(m)]
#print(cond)
k = int(input())
choice = [tuple(map(int, input().split())) for i in range(k)]
ans = 0
for balls in itertools.product(*choice):
    balls = set(balls)
    cnt = sum(A in balls and B in balls for A, B in cond)
    if ans < cnt:
        ans = cnt
print(ans)