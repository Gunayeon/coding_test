# 18 -> 5 5 5 3
# dynamic(18)=dynamic(18-3)+1
# dynamic(15)=dynamic(15-5)+1
# dynamic(10)=dynamic(10-5)+1
# dynamic(5)=dynamic(5-5)+1
# 4 -> 3 1 -? -1
# 6 - 3 3
# 9 -> 3 3 3
# 11 -> 5 3 3

# dynamic(N)=dynamic(N-5)+1
# 조건이 N이 3의 배수일때
# dynamic(N)=min(dynamic(N-5)+1, dynamic(N-3)+1)
import sys
sys.setrecursionlimit(10**6)
N=int(input())
dp=[0]*5010

def dynamic(n):
    result=0
    if dp[n]!=0:
        return dp[n]
    else:
        if n<=0:
            if n==0:
                result=0
            else:
                result=-1
            return result
        else:
            if dynamic(n-3)<0 and dynamic(n-5)<0:
                dp[n]=-1
                result=-1
                return result
            elif dynamic(n-3)>=0 and dynamic(n-5)>=0:
                result=min(dynamic(n-5)+1, dynamic(n-3)+1)
                dp[n]=result
                return result
            elif dynamic(n-3)>=0 and dynamic(n-5)<0:
                result=dynamic(n-3)+1
                dp[n]=result
                return result
            else:
                result=dynamic(n-5)+1
                dp[n]=result
                return result
            

            
print(dynamic(N))
