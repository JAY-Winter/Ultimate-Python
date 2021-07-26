import sys

def fast_plus(N):

    for i in range(N):
        A,B = map(int, sys.stdin.readline().split(''))
        print(A+B)
        if i+1 == N : return

N = int(input())
fast_plus(N)

