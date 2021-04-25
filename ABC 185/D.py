n, m = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
a.append(n)
a.insert(0, 1)
print(a)
b = []
k = float("INF")
for i in range(len(a) - 1):
    t = a[i + 1] - a[i]
    if t != 0:
        b.append(t)
print(b)
k = min(b)
print(k)
ans = 0
for i in b:
    if i == 0:
        pass
    else:
        if i % k == 0:
            ans += (i // k)
        else:
            ans += ((i // k) + 1)
print(ans)
