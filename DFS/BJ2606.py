# DFS : 깊이 우선 탐색 -> 재귀함수
## - Graph(딕셔너리 형태 key:노드, value:해당 노드의 인접노드)
## - start -> 시작점
## - visit 배열
## 1. visit배열에 start 삽입
## 2. 반복문 -> 인접배열 -> 방문 유무 확인 1.방문x -> 해당 노드를 start로 재귀호출

## ex : 바이러스 문제
## 1 : 2, 5
## 2 : 1, 3, 5
## 3 : 2
## 4 : 5, 7
## 5 : 1, 2, 6
## 6 : 5
## 7 : 4
### start = 1, visited=[1], for : 2, 5
#### 2 -> dfs(2) -> visited=[1,2], for : 1, 3 ,5
##### 3 -> dfs(3) -> visited=[1,2,3], for : 2
##### 5 -> dfs(5) -> visited=[1,2,3,5], for : 1,2,6
###### 6 -> dfs(6) -> visited=[1,2,3,5,6], for : 5

num_com=int(input())
num_connected=int(input())
graph=[]
graph_dict={}
for i in range(num_com):
    graph_dict[i+1]=[]

for i in range(num_connected):
    graph.append(list(map(int,input().split())))
    graph_dict[graph[i][0]].append(graph[i][1])
    graph_dict[graph[i][1]].append(graph[i][0])

def make_dfs(graph_dict, start, visited=[]):
    visited.append(start)
    for i in graph_dict[start]:
        if i not in visited:
            make_dfs(graph_dict, i,visited)
    return visited

connected_computer=len(make_dfs(graph_dict,1))-1
print(connected_computer)
