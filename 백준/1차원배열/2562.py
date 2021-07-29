import sys

for i in range(9):

    list = list(map(int, sys.stdin.readline().split()))
    print(list)
    
def max(list):

    point = 0
    max = list[0]

    for i in range(len(list)-1) :

        if max < list[i+1] :
            max = list[i+1]
            point = i+2
            # index 상으로는 i+1 이 맞는데 우리는 몇 번째 위치하는지를 뽑아내야하므로
            # point = i+2 이다
            print(max)
            print( point)
        

max(list)

