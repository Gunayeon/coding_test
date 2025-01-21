# 1 -> 1 -> 1
# 2 -> 1 1 / 2 -> 2
# 3 -> 1 1 1 / 1 2 / 2 1 / 3 -> 4
# 4 -> 1 1 1 1 / 1 1 2 / 1 2 1 / 2 1 1 / .. =-> 7
# dynamic(10)=dynamic(9)
T=int(input())
dp=[0]*12

def dynamic(num):
    result=0
    if dp[num]!=0:
        return dp[num]
    else:
        if num==1 or num==2 or num==3:
            if num==1:
                result=1
            elif num==2:
                result=2
            else:
                result=4
            dp[num]=result
            return result
        else:
            result=dynamic(num-1)+dynamic(num-2)+dynamic(num-3)
            dp[num]=result
            return result

for i in range(T):
    n=int(input())
    print(dynamic(n))       

