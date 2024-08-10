#problem --> https://www.codechef.com/problems/GCEA

# cook your dish here
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    opt=[]
    temp=0
    for i in a:
        if((i*x)>=y):
            opt.append(y)
        else:
            opt.append(i*x)
    for i in opt:
        temp+=i
    print(temp)