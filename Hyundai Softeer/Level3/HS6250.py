N=int(input())
group=[]
for i in range(4):
    if i<3:
        group.append(list(map(int,input().split())))
    else:
        group.append([0]*N)

for i in range(N):
    group[3][i]=group[0][i]+group[1][i]+group[2][i]
    
copy=[row[:] for row in group]


for i in range(4):
    copy[i].sort()

# new_group=group[2][::-1]
# print(new_group)
def orderlist(new_group):
    award={}
    cnt=1
    for i in range(len(new_group)):
        if new_group[i] not in award:
            award[new_group[i]]=cnt
        cnt+=1

    return award



rankings=[orderlist(copy[i][::-1]) for i in range(4)]

for i in range(4):
    result=[]
    for j in range(N):
        result.append(rankings[i][group[i][j]])
    print(" ".join(map(str,result)))