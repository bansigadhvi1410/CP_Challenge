#problem--> https://www.codechef.com/START146D/problems/NOWINNER

# cook your dish here
for _ in range(int(input())):
    a,b,c,m=map(int,input().split())
    scores = sorted([a,b,c])
    diff1 = scores[1] - scores[0]  
    diff2 = scores[2] - scores[1] 
    diff3 = scores[2] - scores[0]
    x=min(diff3,diff2,diff1)
    if x <= m:
      print("Yes")
    else:
        print("No")
    