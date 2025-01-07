import sys
sys.setrecursionlimit(10**6)

N=int(input())
A=list(map(int, input().split()))
op_count=list(map(int,input().split()))






min_cost=1000000000
max_cost=-1000000000

def dfs(cnt=0, cost=A[0]):
    global op_count, min_cost, max_cost
   
    if cnt==N-1:
        min_cost=min(cost, min_cost)
        max_cost=max(cost,max_cost)
       
        return 
    


    # 순회
    for i in range(4):
        # 방문체크
        ## opr[i]=='+'일때 cost+=A[cnt]
        ## opr[i]=='-'일때 cost-=A[cnt]
        ## opr[i]=='*'일때 cost*=A[cnt]
        ## opr[i]=='/'일때 cost/=A[cnt]
        if op_count[i]>0:
            op_count[i] -= 1
            if i==0:
                dfs(cnt+1, cost + A[cnt+1])
            elif i==1:
                dfs(cnt+1, cost - A[cnt+1])
            elif i==2:
                dfs(cnt+1, cost * A[cnt+1])
            elif i==3:
                if cost%A[cnt+1] !=0 and cost*A[cnt+1] <0:
                    dfs(cnt+1, cost//A[cnt+1]+1)
                else:
                    dfs(cnt+1, cost // A[cnt+1])
            op_count[i] += 1

 

dfs()

print(max_cost)
print(min_cost)
