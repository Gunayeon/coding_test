N,K=map(int,input().split())
visited=[0]*100001
def bfs(n,k):
    cnt=0
    queue=[]
    queue.append([n,cnt])
    while len(queue)!=0:
        x, cnt=queue.pop(0)
        dx=[-1,1,x]
        if x==k:
            return cnt
        for i in range(3):
            nx=dx[i]+x
            if nx<0 or nx>100000:
                continue

            if visited[nx]==0:
                visited[nx]=1
                queue.append([nx, cnt+1])

print(bfs(N,K))
