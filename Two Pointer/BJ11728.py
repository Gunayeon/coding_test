# 두 배열 A, B의 크기 입력
N,M=map(int,input().split())


A=list(map(int, input().split()))
B=list(map(int,input().split()))



# 두 포인터 선언
a=0
b=0

# 결과 배열 선언
result=[]

while a<N and b<M:
    # a의 요소가 더 작을때
    if A[a]<B[b]:
        result.append(A[a])
        a+=1
    elif A[a]>B[b]:
        result.append(B[b])
        b+=1
    
if a<N:
    result.extend(A[a:])
if b<M:
    result.extend(B[b:])
print(" ".join(map(str,result)))


