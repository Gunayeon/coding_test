N, B=map(int,input().split())
computer=list(map(int, input().split()))


def check(target):
    sum=0
    for i in range(N):
        if target>computer[i]:
            sum+=(target-computer[i])**2

    if sum>B:
        return False
    else:
        return True

def binarycheck():
    low=0
    high=10**10
    result=0
    while low<=high:
        mid=(low+high)//2
        if check(mid)==False:
            high=mid-1
        else:
            result=mid
            low=mid+1
    return result

print(binarycheck())