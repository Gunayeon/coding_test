import sys
ground=[]
for i in range(3):
    ground.append((list(map(int, sys.stdin.readline().split()))))

cost_result=[]
def getmincost(lst):
    result=[]
    cost=0
    for height in range(1,4):
        cost=0
        for i in range(3):
            cost+=abs(height-lst[i])
        result.append(cost)
    return min(result)



for i in range(3):
    cost_result.append(getmincost(ground[i]))
    column=[row[i] for row in ground]
    cost_result.append(getmincost(column))


print(min(cost_result))