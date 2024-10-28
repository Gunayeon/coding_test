################
# 박성원  : 랜선을 모두 N개의 같은 길이로
# 오영식 : K개의 랜선, 길이는 다 다름
## -> K개의 랜선을 잘라내야함
################
# K : 랜선의 개수, N : 필요한 랜선의 개수 tmp : 랜선의 길이
# K줄 -> 이미 가지고 있는 각 랜선의 길이
# k1 // tmp + k2 // tmp + k3 //tmp + k4 //tmp >= 11(N)
## 가능한 N중 가장 작은 값 -> 따라서 가능한 tmp값 중 가장 큰 값

K, N= map(int, input().split())
arr=[]
for i in range(K):
    arr.append(int(input()))
# print(N)
# print(K)
# print(arr)

low=0
high=2**31-1
tmp=0


# print(high)
while low<=high:
    mid=(low+high)//2
    cnt=0
    len = 0
    for i in arr:
        len=i//mid
        cnt+=len
    if cnt >= N:
        tmp = mid
        low = mid + 1
    else:
        high = mid -1
print(tmp)
