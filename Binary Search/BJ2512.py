import sys
input=sys.stdin.readline

n=int(input())
c=list(map(int,input().split()))
sum=int(input())
arr=[]


low,high=1,max(c)
result=-1

while low<=high:
    mid=(low+high)//2
    s = 0
    for i in range(len(c)):
        if c[i] > mid:
            s += mid
        else:
            s += c[i]

    if s<=sum:
        result=mid
        low = mid + 1
    else:
        high = mid - 1

print(result)







