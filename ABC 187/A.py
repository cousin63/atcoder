x = list(input().split())
suma = 0
sumb = 0
for i in range(len(x[0])):
    suma += int(x[0][i])
for i in range(len(x[1])):
    sumb += int(x[1][i])
print(max(suma,sumb))