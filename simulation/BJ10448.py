K=int(input())

T=[]
for i in range(K):
    T.append(int(input()))


def istriangle(num):
    for i in range(1,50):
        for j in range(1,50):
            for k in range(1,50):
                if i*(i+1)/2 + j*(j+1)/2 + k*(k+1)/2==num:
                    return 1
    return 0



for i in range(K):
    print(istriangle(T[i]))