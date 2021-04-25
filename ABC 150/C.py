import itertools
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
aa = sorted(p)
p = tuple(p)
q = tuple(q)
a = list(itertools.permutations(aa))
cnt = 0
cntp = 0
cntq = 0
for i in a:
    cnt += 1
    if p == i:
        cntp = cnt
    if q == i:
        cntq = cnt
print(abs(cntp-cntq))