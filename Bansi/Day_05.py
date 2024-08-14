#problem --> https://www.codechef.com/problems/MINMXOR

def minxor(n,a):
    temp=0
    for i in range(n):
        temp=temp^a[i]
    ans=temp
    for i in range(n):
        ans=min(ans,temp^a[i])
    return ans
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    print(minxor(n,a))