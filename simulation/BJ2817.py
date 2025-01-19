X=int(input())
N=int(input())

arr=[]

for i in range(N):
    arr.append(list(map(str, input().split())))

for i in range(N):
    arr[i][1]=int(arr[i][1])

lst=[]
for i in range(N):
    if arr[i][1]/X>=0.05:
        for j in range(14):
            lst.append(round(arr[i][1]/(j+1),6))

lst.sort(reverse=True)
sorted_lst=set(lst[0:14])

result=[]
for i in range(N):
    count=0
    if arr[i][1]/X>=0.05:
        for j in range(14):
            if round(arr[i][1]/(j+1),6) in sorted_lst:
                count+=1
        result.append([arr[i][0],count])

result.sort()

for i in range(len(result)):
    print(result[i][0],result[i][1])
