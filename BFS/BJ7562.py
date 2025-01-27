T=int(input())

def bfs(r,c):
    queue=[]
    cnt=0
    queue.append([r,c,cnt])
    
    while len(queue)!=0:
        dr=[1,1,-1,-1,2,2,-2,-2]
        dc=[2,-2,2,-2,1,-1,1,-1]
        r,c, cnt=queue.pop(0)
    
        if r==des_r and c==des_c:
            return cnt
        cnt+=1
        for i in range(8):
            nr=r+dr[i]
            nc=c+dc[i]
            
            if nr<0 or nc<0:
                continue
            elif nr>=l or nc>=l:
                continue
            
            if night[nr][nc]==0:
                night[nr][nc]=1
                queue.append([nr,nc,cnt])
                
             

for i in range(T):
    l=int(input())
    night=[[0]*l for i in range(l)]
    st_r,st_c=map(int,input().split())
    des_r,des_c=map(int,input().split())

    print(bfs(st_r,st_c))





