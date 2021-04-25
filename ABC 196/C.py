x = int(input())
ans = 0
n = len(str(x))

if n % 2 == 1:
    n = n - 1
    print((n // 2) * "9")
    exit()
else:
    while True:
        n = len(str(x))
        if n % 2 == 1:
            n = n - 1
            print((n//2)*"9")
            exit()
        x = str(x)
        a = []
        b = []
        for j in range(n//2):
            a.append(int(x[j]))
            b.append(int(x[(n//2)+j]))
        if a == b:
            #print(a)
            #print(b)
            x = "0"
            for i in a:
                x += str(i)
            x = (int(x))
            #print(x)
            break
        else:
            x = int(x)
            x = x - 1

    aa = int("1"+"0"*(len(a)-1))
    #print(aa)
    y = (x-aa+1)
    if n-1 >= 2:
        z = (((n-1)//2)*"9")
        print(y+int(z))
    else:
        print(x-aa+1)