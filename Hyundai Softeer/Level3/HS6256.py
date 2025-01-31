# N=int(input())
# car_list=[]
# for i in range(N):
#     car_list.append(list(map(str, input().split())))

# for i in range(N):
#     car_list[i][0]=int(car_list[i][0])

# car_dict={}
# for i in range(N):
#     if car_list[i][0] not in car_dict.keys():
#         car_dict[car_list[i][0]]=[]
#     car_dict[car_list[i][0]].append((car_list[i][1],i+1))
   
# print(car_list)
# print(car_dict)

# time=0
# AQueue=[]
# BQueue=[]
# CQueue=[]
# DQueue=[]
# result=[]
# while True:
   
#     if time in car_dict.keys():
#         for i in range(len(car_dict[time])):
#             if car_dict[time][i][0]=='A':
#                 AQueue.append([car_dict[time][i][1],time])
#             elif car_dict[time][i][0]=='B':
#                 BQueue.append([car_dict[time][i][1],time])
#             elif car_dict[time][i][0]=='C':
#                 CQueue.append([car_dict[time][i][1],time])
#             elif car_dict[time][i][0]=='D':
#                 DQueue.append([car_dict[time][i][1],time])

#     # 예외 1 : 반대 방향차들이 동시에 있을 경우
#     # if len(AQueue)!=0 and len(CQueue)!=0
#     # if 'A' in car_dict[time][i]

#     if len(DQueue)==0 and len(AQueue)!=0:
#         go=AQueue.pop(0)[1]
#         result.append([time,('A',go)])
        
#     elif len(AQueue)==0 and len(BQueue)!=0:
#         go=BQueue.pop(0)[1]
#         result.append([time,('B',go)])
        
#     elif len(BQueue)==0 and len(CQueue)!=0:
#         go=CQueue.pop(0)[1]
#         result.append([time,('C',go)])
        
#     elif len(CQueue)==0 and len(DQueue)!=0:
#         go=DQueue.pop(0)[1]
#         result.append([time,('D',go)])
       
#     print(result)
   
#     time+=1
#     if len(result)==len(car_list):
#         break

# print(result)
from collections import deque
N=int(input())
car_list=[]
for i in range(N):
    car_list.append(list(map(str, input().split())))

for i in range(N):
    car_list[i][0]=int(car_list[i][0])
time=0
car_index=0
result=[-1]*N


AQueue=deque()
BQueue=deque()
CQueue=deque()
DQueue=deque()
Queue=[AQueue,BQueue,CQueue,DQueue]
dic_que={'A':0, 'B':1, 'C':2, 'D':3}
dic_right={0:3,1:0,2:1,3:2}

def car_in():
    global car_index
    # if car_index>=N:
    #     return
    while car_index < N and car_list[car_index][0]==time:
        Queue[dic_que[car_list[car_index][1]]].append(car_index)
        car_index+=1
def car_out():
    out_list=[]
    # A,B,C,D 확인
    for i in range(4):
        # 오른쪽에 있는경우가 아닐경우에 들어감 : 동시도 가능
        if len(Queue[dic_right[i]])==0 and len(Queue[i])!=0:
            out_list.append(i)
    for i in out_list:
        now=Queue[i].popleft()
        result[now]=time
def time_flow():
    # 낙동강 오리알 방지
    global time
    if car_index<N and len(Queue[0])==0 and len(Queue[1])==0 and len(Queue[2])==0 and len(Queue[3])==0:
        time=car_list[car_index][0]
    else:
        time+=1

while True:
    car_in()
    car_out()
    time_flow()
  
    # 종료조건 1 : car_index=N 이고 Queue에 아무것도 없을떄
    if car_index==N and len(Queue[0])==0 and len(Queue[1])==0 and len(Queue[2])==0 and len(Queue[3])==0:
        break
    # 종료조건 2 : 교착상태
    elif len(Queue[0])!=0 and len(Queue[1])!=0 and len(Queue[2])!=0 and len(Queue[3])!=0:
        break

for i in range(N):
    print(result[i])
    
