import sys

K, P, N = map(int, sys.stdin.readline().split())





result=K
for i in range(N):
    result*=P

print(result)