import sys
N=int(sys.stdin.readline())

arr=[]
for i in range(N):
    arr.append(list(map(str, sys.stdin.readline().split())))
    



def whereX(msg):
    return msg.find('X')


sum=[]
for i in range(N):
    sum.append(arr[i][1][whereX(arr[i][0].upper())].upper())
   
print(''.join(map(str,sum)))



