N, B=map(int,input().split())
number='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer=''

while N>0:
    answer+=number[N%B]
    N=N//B

print(answer[::-1])
