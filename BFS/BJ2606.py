N=int(input())
T=int(input())
com=[]
for i in range(T):
    com.append(list(map(int,input().split())))
com_dict={}
for i in range(N):
    com_dict[i+1]=[]

for i in range(T):
    com_dict[com[i][0]].append(com[i][1])
    com_dict[com[i][1]].append(com[i][0])

visit=[0]*N

def bfs():
    queue=[]
    queue.append(1)
    visit[0]=1
    cnt=0
    while len(queue)!=0:
        now=queue.pop(0)
        for i in com_dict[now]:
            if visit[i-1]==0:
                visit[i-1]=1
                cnt+=1
                queue.append(i)
     
    return cnt

print(bfs())