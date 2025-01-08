N, M=map(int,input().split())
A=list(map(int,input().split()))
print(A)

i=0
j=0

count=0
while j<N:
    if sum(A[i:j+1])==M:
        count+=1
        i+=1
        j+=1
    elif sum(A[i:j+1])>M:
        i+=1
    else:
        j+=1

print(count)
