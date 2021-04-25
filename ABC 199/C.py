n = int(input())
sa = list(range(n))
sb = list(range(n,2*n))
S = list(input())
q = int(input())
#print(sa,sb)
for i in range(q):
    t,a,b = map(int,input().split())
    if t == 1:
        a = a - 1
        b = b - 1
        if b+1 <= n:
            #print("a")
            sa[a], sa[b] = sa[b], sa[a]
        elif n < a+1:
            #("b")
            sb[a - n], sb[b - n] = sb[b - n], sb[a - n]
        elif a+1<=n and b+1>= n:
            #print("c")
            sa[a], sb[b - n] = sb[b - n], sa[a]
        #print(sa,sb)
    if t==2:
        #print(2)
        sa,sb = sb,sa
        #print(sa, sb)

ans = []
for i in range(n):
    ans.append(S[sa[i]])
for i in range(n):
    ans.append(S[sb[i]])
print(*ans,sep="")