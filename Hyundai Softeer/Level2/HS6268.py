import sys
T=int(sys.stdin.readline())
case=[]
for i in range(T):
    case.append(list(map(str, input().split())))

light={'':[0,0,0,0,0,0,0],'1':[0,0,1,0,0,0,1],'2':[1,0,1,1,1,1,0],
       '3':[1,0,1,1,0,1,1],'4':[0,1,1,1,0,0,1],'5':[1,1,0,1,0,1,1],
       '6':[1,1,0,1,1,1,1],'7':[1,1,1,0,0,0,1],'8':[1,1,1,1,1,1,1],
       '9':[1,1,1,1,0,1,1],'0':[1,1,1,0,1,1,1]}

def change(a,b):
    sum=0
    for i in range(7):
        sum+=abs(light[a][i]-light[b][i])

    return sum




result=[]
for k in range(T):
    i=0
    sum=0
    while True:
        if i>=len(case[k][0]) and i<len(case[k][1]):
            a=''
        
            b=case[k][1][len(case[k][1])-i-1]
            sum+=change(a,b)
        elif i<len(case[k][0]) and i>=len(case[k][1]):
            a=case[k][0][len(case[k][0])-i-1]
            b=''
            sum+=change(a,b)
        elif i<len(case[k][0]) and i<len(case[k][1]):
            a=case[k][0][len(case[k][0])-i-1]
            b=case[k][1][len(case[k][1])-i-1]
            sum+=change(a,b)
        elif i>=len(case[k][0]) and i>=len(case[k][1]):
            break
        
        i+=1
    result.append(sum)


for i in range(T):
    print(result[i])


