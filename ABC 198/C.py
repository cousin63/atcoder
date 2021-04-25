r,x,y = map(int,input().split())
mind = ((x**2)+(y**2))**(0.5)
#print(mind)
if mind%r==0:
    print(int(mind//r))
else:
    print(int(mind//r)+1)