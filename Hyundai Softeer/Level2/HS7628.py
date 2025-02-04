import sys
n=int(sys.stdin.readline())

arr=list(map(int, input().split()))

def get(lst,target):
    result=[]
    for i in range(len(lst)):
        result.append(lst[i]%target)

    return result.count(0)



result=[]
for i in range(2,101):
    result.append(get(arr, i))
    
print(result)
print(max(result))