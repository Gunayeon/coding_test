n, q=map(int,input().split())
car_list=list(map(int,input().split()))
m=[]
for i in range(q):
    m.append(int(input()))

car_list.sort()

def whatisM(lst,target):
    left=0
    right=len(lst)-1
   
    while left<=right:
        
        mid=(left+right)//2
        if lst[mid]>target:
            right=mid-1
        elif lst[mid]<target:
            left=mid+1
        else:
            return mid
    if left>right:
        return 0
    




for i in range(q):
    low=whatisM(car_list,m[i])
    high=len(car_list)-(whatisM(car_list,m[i])+1)
    print(low*high)
