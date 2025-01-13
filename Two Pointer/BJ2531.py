N, d, k, c = map(int, input().split())


chobab=[]
for i in range(N):
    chobab.append(int(input()))


visited=[0]*d
visited[c-1]=1

count=1
max_count=-100000000

for i in range(k):
    visited[chobab[i]-1]+=1
    if visited[chobab[i]-1]==1:
        count+=1
max_count=count

start=0
end=k
while start<N:
    visited[chobab[start]-1]-=1
    if visited[chobab[start]-1]==0:
        count-=1

    visited[chobab[end]-1]+=1
    if visited[chobab[end]-1]==1:
        count+=1

    start+=1
    end+=1
    if end==N:
        end=0
    if max_count<count:
        max_count=count
print(max_count)

