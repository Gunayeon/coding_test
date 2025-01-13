S, P = map(int, input().split())
dna=input()
str_count=list(map(int, input().split()))
start=0
end=P-1
arr=[0]*4
acgt=['A', 'C', 'G', 'T']
count=0


for i in range(4):
    arr[i]=dna[start:end+1].count(acgt[i])


if arr[0]>=str_count[0] and arr[1]>=str_count[1] and arr[2]>=str_count[2] and arr[3] >= str_count[3]:
    count+=1

start+=1
end+=1
while end<S:
    for i in range(4):
        if dna[start-1]==acgt[i]:
            arr[i]-=1

    for i in range(4):
        if dna[end]==acgt[i]:
            arr[i]+=1

    if arr[0]>=str_count[0] and arr[1]>=str_count[1] and arr[2]>=str_count[2] and arr[3] >= str_count[3]:
        count+=1
    start+=1
    end+=1

print(count)

