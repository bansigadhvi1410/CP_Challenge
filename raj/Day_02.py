# Question -> https://www.codechef.com/problems/BUDGET25?tab=statement
# cook your dish here
for i in range(int(input())):
    n, x = map(int, input().split())
    ln = list(map(int, input().split()))
    
    c = 0
    surplus = 0
    for i in range(n):
        if ln[i] > x:
            diff = ln[i] - x
            ln[i] -= diff
            surplus += diff

    ln.sort()                                
    
    for i in range(n-1, -1, -1):
        if ln[i] < x and surplus >= x - ln[i]:
            don = x - ln[i]
            ln[i] += don
            surplus -= don
    
    for i in range(n):
        if ln[i] >= x:
            c += 1
    
    print(c)
