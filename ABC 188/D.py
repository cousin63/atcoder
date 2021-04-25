n,c = map(int,input().split())

demand = [0] * 220000
for _ in range(n):
    a, b, t = map(int, input().split())
    if t<c:
        demand[a] += t
        demand[b] -= t
    elif t>=c:
        demand[a] += c
        demand[b] -= c

for i in range(1,220000):
    if demand[i-1]>=c:
        demand[i] += c
    else:
        demand[i] += demand[i - 1]

print(sum(demand))