h ,w = map(int,input().split())
a = [list(map(int, input().split())) for i in range(h)]
minlist = []
suma = []
for i in range(h):
    minlist.append(min(a[i]))
    suma.append(sum(a[i]))
print(sum(suma)-(min(minlist)*h*w))