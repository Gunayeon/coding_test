N,M=map(int,input().split())

miro=[]
for i in range(N):
    miro.append(list(map(int,input())))



visit=[[0]*M for _ in range(N)]

def bfs():
    queue=[]
    start=(0,0)
    queue.append([start,1])
    while len(queue)!=0:
        now,distance=queue.pop(0)
        
        r=now[0]
        c=now[1]
        dr=[-1,1,0,0]
        dc=[0,0,-1,1]
        
        # 종료 조건
        if r==N-1 and c==M-1:
            return distance
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
           
            if nr<0 or nc<0:
                continue
            elif nr>=N or nc>=M:
                continue

            if visit[nr][nc]==0 and miro[nr][nc]==1:
                visit[nr][nc]=1
                
                queue.append([(nr,nc),distance+1])
        


print(bfs()) 