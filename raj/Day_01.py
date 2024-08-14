for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    mini=min(a);maxi=max(a)
    if mini==maxi:print("yes")
    else:
        a=list(set(a))
        if len(a)==2 and mini==0 and maxi in a:print("yes")
        else:print("no")
    
