T=int(input())

# 5*4*3*2*1/(4*3*2*1) * 1
# M!/(M-N)!N!

dp=[0]*31


def factorial(N):
    result=0
    if dp[N]!=0:
        return dp[N]
    else:
        if N==1 or N==0:
            result=1
            dp[N-1]=1
            return result
        else:
            result = N * factorial(N-1)
            dp[N]=result
            return result

for i in range(T):
    N, M= map(int, input().split())
    
    print(int(factorial(M)/(factorial(N)*factorial(M-N))))

