import sys

N = list(map(int, sys.stdin.readline().split()))
# X = map(int, sys.stdin.readline())
X = int(input())
def smaller(N,X):
    
        for j in range(len(N)):
            if N[j] < X : print(N[j], end=" ")

smaller(N,X)

# N == 10 
# 10 개의 수로 이루어진 수열
# X == 5
# 수열 중 5보다 작은 수     