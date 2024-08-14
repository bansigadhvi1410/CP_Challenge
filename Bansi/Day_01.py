# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    minn=min(a)
    maxx=max(a)
    a=set(a)
    if len(a)==1 or (len(a)==2 and minn==0 and maxx in a):
        print("Yes")
    else:
        print("No")