n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = []
for i in range(n):
    ans.append(a[i]*b[i])
if sum(ans)==0:
    print("Yes")
else:
    print("No")