T=int(input())

test=[]
for i in range(T):
    test.append(int(input()))

def changetoB(num,B):
    answer=[]
    while num>0:
        answer.append(str(num%B))
        num=num//B
    return answer[::-1]

def check(lst):
    count=0
    for i in range(len(lst)//2):
        if lst[i]==lst[len(lst)-1-i]:
            count+=1
    
    if count==len(lst)//2:
        return 1
    
    return 0

        



for i in range(T):
    result=0
    for b in range(2, 65):
        if check(changetoB(test[i],b)):
            result=1
          
            
    print(result)
