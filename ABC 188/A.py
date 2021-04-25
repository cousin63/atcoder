x,y = map(int,input().split())
if (max(x,y)-min(x,y)) < 3:
    print("Yes")
else:
    print("No")