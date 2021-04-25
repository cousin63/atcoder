n = int(input())
a = list(map(int,input().split()))
b = a[2**(n-1):]
a = a[:2**(n-1)]

if max(a)<max(b):
    print(a.index(max(a))+1)
else:
    print(b.index(max(b))+1+2**(n-1))