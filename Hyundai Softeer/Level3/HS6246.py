import sys
sys.setrecursionlimit(10**6)
n, m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

placelist=[]
for i in range(m):
    placelist.append(list(map(int, input().split())))


visited=[[0]*n for i in range(n)]
result=0

visitplace=placelist[1:-1:]

def dfs(start_r, start_c, end_r, end_c,check):
    global visited,arr,result

    dr=[-1,1,0,0]
    dc=[0,0,-1,1]
   
    
    if start_r==end_r and start_c==end_c and check==len(visitplace):
        result+=1
        check=0
        return 
    
    if check!=len(visitplace) and start_r==visitplace[check][0]-1 and start_c==visitplace[check][1]-1:
        check+=1
       
  
    visited[start_r][start_c]=1
   
    for i in range(4):
        nr=start_r+dr[i]
        nc=start_c+dc[i]

        if nr<0 or nc<0:
            continue
        elif nr>=3 or nc>=3:
            continue

        if visited[nr][nc]==0 and arr[nr][nc]==0:
            dfs(nr,nc,end_r,end_c,check)
    visited[start_r][start_c]=0


dfs(placelist[0][0]-1,placelist[0][1]-1,placelist[n-1][0]-1,placelist[n-1][1]-1, 0)
print(result)
