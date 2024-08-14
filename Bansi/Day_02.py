#problem --> https://www.codechef.com/problems/BUDGET25?tab=statement

# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    greater=0
    lesser=-1
    count=0
    for i in range(n):
        if(a[i]>x):
            greater+=(a[i]-x)
            count+=1 
        else:
            lesser=i 
            break
    if lesser==-1:
        print(count)
    else:
        for i in range(lesser,n):
            greater-=(x-a[i])
            if greater>=0:
                count+=1 
            else:
                break 
        print(count)
