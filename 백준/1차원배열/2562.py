
def max():

    List = []
    
    for i in range(9):

        num = int(input())
        List.append(num)

    max = List[0]
    point = 0

    for i in range(len(List)-1) :

        if max < List[i+1] :
            max = List[i+1]
            point = i+2
            # index 상으로는 i+1 이 맞는데 우리는 몇 번째 위치하는지를 뽑아내야하므로
            # point = i+2 이다
    print(max)
    print(point)
        

max()


