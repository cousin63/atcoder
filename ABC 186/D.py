n = int(input())
a = list(map(int,input().split()))
lista = []
for i in range(n-1):
    for j in range(i+1,n):
        lista.append(abs(a[i]-a[j]))
print(sum(lista))