import sys
N=int(input())
M=int(input())
x=list(map(int, input().split()))

def check(target):
    for i in range(len(x)):
        # 첫번째 위치
        if i==0:
            if x[i]-target<=0:
                continue
            else:
                return False
    
        else:
            if x[i-1]+target>=x[i]-target:
                continue
            else:
                return False
    # 마지막 위치, x의 길이가 1일때도 가로등이 마지막위치까지 불을 비추는지 확인하는 조건문
    if x[len(x)-1] + target >= N:
        return True
    else:
        return False


def binary(N):
    low=0
    high=N
    result=0

    while low<=high:
        mid = (low + high) // 2
        # 왼쪽 탐색
        if check(mid):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result

print(binary(N))












