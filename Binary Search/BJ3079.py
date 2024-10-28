import sys
N, M = map(int, input().split())
T=[]
for i in range(N):
    T.append(int(input()))


low=0
high=sys.maxsize


def check(time):
    cnt = 0
    for i in T:
        cnt+=time//i

    return cnt


answer=0
while low<=high:
    mid=(low+high)//2
    if check(mid)>=M: # 명수가 더 많음 -> 시간이길다는말 -> 왼쪽탐색
        answer=mid
        high=mid-1
    else:
        low=mid+1

print(answer)




