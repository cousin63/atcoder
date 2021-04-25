x = list(input())
y = []
for i in range(len(x)):
    if x[i]== '.':
        break
    y.append(int(x[i]))
print(*y,sep="")