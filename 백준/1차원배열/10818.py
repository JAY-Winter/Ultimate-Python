import sys
N  = int(input())

list = list(map(int, sys.stdin.readline().split()))

def max_min(N,list):

    min = list[0]
    max = list[0]

    for i in range(N-1):
        
        if min > list[i+1] :
            min = list[i+1]

        elif max < list[i+1]:
            max = list[i+1]

    print(min, max)

max_min(N,list)