
# 0(0->0), 10(0->1), 15(0->2), 20(0->3)
# 5(1->0), 0 (1->1),  9(1->2), 10(1->3)
# 6(2->0), 13(2->1),  0(2->2), 12(2->3)
# 8(3->0),  8(3->1),  9(3->2), 0(3->3)
# 10 9 12 8


# 필요한 요소-> 최소 비용, 방문 배열, 입력, DFS
## 방문배열 visited =[] -> 방문하면 1, 방문안하면 0
## DFS : 시작 위치, 현재 위치, 방문 횟수 ,배용
### 모든 도시를 방문한 경우 -> 혅재도시에서 시작 도시로 돌아올 수 있는 경우 최소비용 계산
### 모든 도시 순회 -> 도시의 개수만큼 반복
#### 다른도시 방문x, 현재도시에서 다른도시로 넘어가는 비용이 0이 아닐때
#### -> 다음 도시 방문처리, dfs호출, 백트래킹 위해 방문취소
import sys
N=int(input())
W=[]
min_cost=sys.maxsize
for i in range(N):
    W.append(list(map(int, input().split())))
# print(W)

def dfs(start, now, count, cost):
    global visited,min_cost

    if count==N:
        if W[now][start]!=0:
            min_cost=min(min_cost, cost+W[now][start])
        return

    for next in range(N):
        if visited[next]==0 and W[now][next]!=0:
            visited[next]=1
            # 순회하는동안 처음위치는 바뀐것이 아니므로 고정이다.
            dfs(start,next,count+1,cost+W[now][next])
            visited[next]=0 # 시작위치 방문후 다음 경로의 경우의수를 포함하기위해 다시 0으로 바꿔준다

for start in range(N):
    visited = [0 for i in range(N)] # 시작 위치마다 경로를 다시 탐색해야하므로 항상 초기화해준다
    visited[start]=1
    dfs(start,start,1,0)

print(min_cost)





