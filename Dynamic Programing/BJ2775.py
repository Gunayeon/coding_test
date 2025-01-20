# a층의 b호 = a-1층 1호부터 b호합
# k층, n호
# 1 3 -> 1층 3호 -> 0층 1호 1명 + 0층 2호 2명 + 0층 3호 3명
# 2 3 -> 2층 3호 -> 1층 1호(1) + 1층 2호(1+2) + 1층 3호(1+2+3)

# 3 3 -> 3층 3호 -> 2층 1호(1층 1호(1))+ 2층 2호(1층 1호(1), 1층 2호(1+2)) + 2층 3호
T=int(input())
dp=[[0]*15 for i in range(15)] 

def dynamic(a,b):
    if dp[a][b]!=0:
        return dp[a][b]
    else:
        result=0
        if a==0:
            result=b
            dp[a][b]=result
            return result
        else:
            for i in range(1,b+1):
                result+=dynamic(a-1,i)

            dp[a][b]=result
         
            return result

for i in range(T):
    k=int(input())
    n=int(input())

    print(dynamic(k,n))
    

