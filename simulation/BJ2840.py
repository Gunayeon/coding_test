N, K=map(int,input().split())



arr=[]

for i in range(K):
    arr.append(list(map(str, input().split())))

for i in range(K):
    arr[i][0]=int(arr[i][0])

circle=[0]*N
now=0
for i in range(K-1,-1,-1):
    if i==K-1:
        circle[K-i-1]=arr[i][1]
    else:
        now+=(arr[i+1][0])
        now%=N

        if circle[now]==0 or circle[now]==arr[i][1]:
            circle[now]=arr[i][1]
        elif circle[now]!=arr[i][1] and circle[now]!=0:
            circle[now]='!'
            
result=''
result_set=set()
for i in range(N):
    if circle[i]==0:
        circle[i]='?'
    result+=circle[i]

    result_set.add(circle[i])


if '!' in result:
    print('!')
elif '?' in result:
    if len(result_set)!=len(result)-result.count('?')+1:
        print('!')
    else:
        print(result)
else:
    if len(result_set)!=len(result):
        print('!')
    else:
        print(result)