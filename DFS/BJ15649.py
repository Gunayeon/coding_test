import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split()) 
visited=[]
arr=[]
def dfs(start):
    global visited, N,M,arr
    
    
    

    if len(visited)==M:
        arr.append(visited[:])
        return
    
    for next in range(1,N+1):
       
        if next not in visited:

            visited.append(next)
            dfs(next)

            visited.remove(next)

dfs(1)

for i in range(len(arr)):
    print(" ".join(map(str, arr[i])))
    
