n = int(input())
boollist = [True]*(n+1)
boollist[0] = False
for i in range(1,n+1):
    if "7" in str(i):
        boollist[i] = False
for i in range(1,n+1):
    if "7" in str(oct(i)):
        boollist[i] = False
print(sum(boollist))