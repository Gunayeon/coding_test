import sys
N, M=map(int, sys.stdin.readline().split())

time_schedule=[0]*18


room_list=[]
reservation=[]
for i in range(N):
    room_list.append(input())

for i in range(M):
    reservation.append(list(map(str, sys.stdin.readline().split())))
    reservation[i][1]=int(reservation[i][1])
    reservation[i][2]=int(reservation[i][2])


match_room={}
for i in range(N):
    match_room[room_list[i]]=[0]*18


i=0
result={}
for i in range(M):
    if 1 not in match_room[reservation[i][0]][reservation[i][1]:reservation[i][2]]:
        for k in range(reservation[i][2]-reservation[i][1]):
            match_room[reservation[i][0]][reservation[i][1]+k]=1

cnt=0

for i in range(N):
    cnt=0
    start=0
    result[room_list[i]]=[]
    for k in range(9,18):
        if match_room[room_list[i]][k]==0:
            if start==0:
                start=k
            cnt+=1
           

            if k==17 and start!=0:
                result[room_list[i]].append([start,start+cnt])

        elif match_room[room_list[i]][k]==1:
            if k!=9 and start!=0:
                result[room_list[i]].append([start,start+cnt])
            cnt=0
            start=0


room_list.sort()

for i in range(N):
    print(f'Room {room_list[i]}:')
    if len(result[room_list[i]])==0:
        print("Not available")
    else:
        
        print(f'{len(result[room_list[i]])} available:')
        for j in range(len(result[room_list[i]])):
          
            if len(str(result[room_list[i]][j][0]))==1:
                start='0'+str(result[room_list[i]][j][0])
            elif len(str(result[room_list[i]][j][0]))==2:
                start=str(result[room_list[i]][j][0])

            if len(str(result[room_list[i]][j][1]))==1:
                end='0'+str(result[room_list[i]][j][1])
            elif len(str(result[room_list[i]][j][1]))==2:
                end=str(result[room_list[i]][j][1])
            
            print(start+'-'+end)
    if i<N-1:
        print('-----')
        


