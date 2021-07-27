import sys

def Beautiful_plus(N):

    for i in range(N):

        A,B = map(int,sys.stdin.readline().split())
        result = A+B

        case = 'Case #{index}: {A} + {B} = {result}'.format(index = i+1, A=A, B=B, result = A+B)
        print(case)

N = int(input())

Beautiful_plus(N)