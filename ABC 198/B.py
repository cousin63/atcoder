n = input()

def ispalindrome(str): return 1 if str == str[::-1] else 0

while True:
    if n[-1:]=="0":
        n = n[:-1]
    else:
        break

if ispalindrome(n)==0:
    print("No")
else:
    print("Yes")