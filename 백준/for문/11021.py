import sys

def f_plus(N):

    for i in range(N):

        A,B = map(int,sys.stdin.readline().split())

        case = ('Case #{index}: {result}').format(index = i+1, result = A+B)
        print(case)

N = int(input())
f_plus(N)

