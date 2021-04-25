n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
aa = max(a)
bb = min(b)
if bb>=aa:
    print(bb-aa+1)
else:
    print(0)