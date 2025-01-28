from collections import deque
M,N=map(int,input().split())

tomato=[]
for i in range(N):
    tomato.append(list(map(int,input().split())))


visited=[[0]*M for _ in range(N)]
def bfs():
    queue=deque()
    cnt=0
    tomato_cnt=0
    day=0
    for i in range(N):
        for j in range(M):
            if tomato[i][j]==1:
                visited[i][j]=1
                queue.append((i,j,day))
            
            if tomato[i][j]==0:
                tomato_cnt+=1

    while len(queue)!=0:
        row,col,day=queue.popleft()
      
        dr=[-1,1,0,0]
        dc=[0,0,-1,1]
        
        for i in range(4):
            nr=dr[i]+row
            nc=dc[i]+col

            if nr<0 or nc<0:
                continue
            elif nr>=N or nc>=M:
                continue

            if visited[nr][nc]==0 and tomato[nr][nc]==0:
                visited[nr][nc]=1
                cnt+=1
                # pop기준으로 +1만
                queue.append((nr,nc,day+1))
       

 
    if cnt==tomato_cnt:
        return day
    else:
        return -1
print(bfs())
