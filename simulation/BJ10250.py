T=int(input())

for i in range(T):
    H,W,N=map(int,input().split())
    if N%H==0:
        X=str(H)
        Y=str(N//H)
    else:
        X=str(N%H)
        Y=str(N//H+1)


    if len(Y)==1:
        Y='0'+Y
    print(X+Y)