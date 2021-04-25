a,b,x,y = map(int,input().split())
if a == b:
    print(x)
    exit()
if a<b:
    rouka = ((b-a)*2+1)*x
    kaidan = (b-a)*y+x
    if rouka <= kaidan:
        print(rouka)
    else:
        print(kaidan)
if b<a:
    rouka = (((a-b)*2)-1)*x
    kaidan = (a-b-1)*y+x
    if rouka <= kaidan:
        print(rouka)
    else:
        print(kaidan)