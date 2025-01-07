import sys
sys.setrecursionlimit(10**6)

n=int(input())
k=int(input())

card=[]
for i in range(n):
    card.append(input())


visited=[0]*n
answer=set()
def dfs(count=0, cost=''):
    global visited

    # 종료 조건
    if count==k:
        answer.add(cost)
        return
    
    # 순회
    for i in range(n):
        # 방문 체크 : 방문 안했을때
        if visited[i]==0:
            visited[i]=1
            dfs(count+1, cost+card[i])
            visited[i]=0



dfs()
print(len(answer))