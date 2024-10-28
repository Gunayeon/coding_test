# 게임횟수 : X
# 이긴게임 : Y
# 승률 : Z = int((X / Y) * 100)

# 최소 몇판 더 해야하는 지 -> 추가횟수 : tmp
## int(((X+tmp) / (Y+tmp)) * 100)-int((X / Y) * 100) 가 최소 1이상

# 우리가 찾고자하는건 tmp

# 예외 : Z가 절대 변하지 않을떄
# 1. X==Y
import sys


## low <= high까지 loop
#### low, high, mid=(low+high)//2
#### int(((X+tmp) / (Y+tmp)) * 100)-int((X / Y) * 100) 가 최소 1이상
#### 저 위 조건 만족하면 tmp를 mid에 넣음 -> 만족하는 값중에 가장 작은값을 찾아야함
##### high가 mid-1, low는 그대로
#### 만족하지 않으면
##### low가 mid+1
import sys
X, Y= map(int, input().split())

Z = Y*100//X
low = 0
tmp = -1
high = 2100000000

while low <= high:
    mid = (low + high) // 2
    if (Y+mid)*100//(X+mid)-Z>=1:
        tmp = mid
        # print("추가횟수:",tmp)
        high = mid -1
        # print("끝",high)
    else:
        low = mid + 1
        # print("시작",low)
print(tmp)






