n=int(input())
a=list(map(int, input().split()))
target=int(input())

# 두 포인터
i=0
j=n-1

a.sort()

# 개수 세기
count=0
while i<j:
    if a[i]+a[j]==target:
        count+=1
        i+=1
        j-=1
    elif a[i]+a[j]>target:
        j-=1
    else:
        i+=1
print(count)



    