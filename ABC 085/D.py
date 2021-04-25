n, h = map(int, input().split())
shake = []
throw = []
for i in range(n):
    a, b = map(int, input().split())
    shake.append(a)
    throw.append(b)
maxshake = max(shake)
threw = []
for i in range(n):
    if throw[i] > maxshake:
        threw.append(throw[i])
threw.sort(reverse=True)

while True:
    if h <= sum(threw):
        for i in range(len(threw)):
            h -= threw[i]
            if h <= 0:
                print(i+1)
                exit()
    else:
        h -= sum(threw)
        if h%maxshake==0:
            print((h // maxshake) + len(threw))
            exit()
        else:
            print((h // maxshake) + len(threw)+1)
            exit()