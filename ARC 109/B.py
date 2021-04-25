import math
n = int(input())
a = n+1
i = n-109109108641970782
print(i)
print(n//i)
ans = (1+i)*i//2
if ans > a:
    while True:
        if ans < a:
            print(a-i)
            exit()
        ans -= i
        i -= 1
if ans < a:
    while True:
        if ans > a:
            print(a-i+1)
            exit()
        ans += i+1
        i += 1