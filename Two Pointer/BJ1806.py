N, S=map(int,input().split())
arr=list(map(int,input().split()))

start=0
end=0
min_length=100000000
sum=arr[start]

length=0
while end<N and (start<=end):
    print(sum)
    if sum<S:
        end+=1
        if end==N:
            continue
        sum+=arr[end]
    else:
        length=end-start+1
        min_length=min(length,min_length)
        if sum==S:
            end+=1
            if end==N:
                continue
            sum+=arr[end]
           
        
        sum-=arr[start]
        start+=1
    
  
if min_length==100000000:
    min_length=0
   

print(min_length)