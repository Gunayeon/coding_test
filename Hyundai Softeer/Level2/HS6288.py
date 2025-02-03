import sys

W, N=map(int,input().split())

MP=[]
for i in range(N):
    MP.append(tuple(map(int, sys.stdin.readline().split())))
sorted_MP=sorted(MP,key=lambda x: x[1], reverse=True)


cost=0

i=0
while True:
    if sorted_MP[i][0]<=W:
        cost+=sorted_MP[i][0]*sorted_MP[i][1]
        W-=sorted_MP[i][0]
    elif sorted_MP[i][0]>W:
        cost+=W*sorted_MP[i][1]
        W=0

    if W<=0:
        break
    if i==N-1:
        break  
    i+=1

print(cost)
        

