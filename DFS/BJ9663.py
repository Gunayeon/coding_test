import sys
sys.setrecursionlimit(10**6)

# 입력
N=int(input())

visited=[0] * N

# 퀸이 위치에 놓을 수 있는지 유무 체크
def check(r,c):
    
    if r==0:
        return True
    
    for i in range(r):
        if c==visited[i]:
            return False
        
        if abs(r-i) ==abs(visited[i]-c):
            return False
        
    return True
count=0   
def dfs(r=0):
    global visited,count

  
    
    if r==N:
        count+=1
        return
    
    for i in range(N):
        if check(r,i):
            visited[r]=i
    
            dfs(r+1)
            visited[r]=0


dfs()
print(count)