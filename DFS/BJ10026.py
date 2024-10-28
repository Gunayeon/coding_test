import sys
sys.setrecursionlimit(10**6)

N=int(input())
pic=[]
pic_arr1=[[0 for i in range(N)] for j in range(N)]
pic_arr2=[[0 for i in range(N)] for j in range(N)]

for i in range(N):
    pic.append(input())
# 적록색약x -> 빨=0, 초 =1/파 =2
# 적록색약 -> 빨, 초 =0/파 =1
for i in range(N):
    for j in range(N):
        if pic[i][j]=='R':
            pic_arr1[i][j] = 0
            pic_arr2[i][j] = 0

        elif pic[i][j]=='G':
            pic_arr1[i][j] = 1
            pic_arr2[i][j] = 0
        elif pic[i][j]=='B':
            pic_arr1[i][j] = 2
            pic_arr2[i][j]=1


def dfs(r,c,m,color):
    dr=[-1,1,0,0]
    dc=[0,0,1,-1]

    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]

        if nr < 0 or nc < 0:
            continue
        elif nr>=N or nc>=N:
            continue

        if m[nr][nc]==color:
            m[nr][nc]=-1
            dfs(nr,nc,m,color)

count_pic1=0
count_pic2=0
for i in range(N):
    for j in range(N):
        if pic_arr1[i][j]!=-1:
            color = pic_arr1[i][j]
            # 첫방문 위치 방문처리 -> 안하면 dfs처럼 작동안함, 모양 맞춤
            pic_arr1[i][j]=-1
            dfs(i,j,pic_arr1,color)
            count_pic1+=1

        if pic_arr2[i][j] != -1:
            color = pic_arr2[i][j]
            pic_arr2[i][j] = -1
            dfs(i, j, pic_arr2, color)
            count_pic2 += 1



print(count_pic1,count_pic2)
