#problem --> https://www.codechef.com/problems/KNOCKOUT?tab=statement

for _ in range(int(input())):
    a=list(map(int,input().split()))
    asort=sorted(a)
    l=dict()
    l[asort[0]]=0
    l[asort[len(a)-1]]=4
    for i in range(1,len(asort)):
        if i<3:
            l[asort[i]]=1
        elif i<7:
            l[asort[i]]=2
        elif i<15:
            l[asort[i]]=3
    for i in range(len(a)):
        print(l[a[i]] , end=' ')