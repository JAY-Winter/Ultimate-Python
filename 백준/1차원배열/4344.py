# import sys

# C = int(input())

# def over_ave(C):

#     answer = []

#     for i in range(C):

#         score = list(map(int, sys.stdin.readline().split()))
#         N  = score[0]
#         ave = (sum(score)-N)/N
#         count = 0

#         for j in range(N+1):

#             if score[j] > ave : count += 1
                
#             over_students_ave = (count/N)*100            
#             round(over_students_ave)

#         answer.append("%0.3f" %+over_students_ave+"%")

#     for k in range(len(answer)):

#         print(answer[k])

# over_ave(C)



C = int(input())

for test_case in range(C) :
    
    case = list(map(int, input().split()))

    N = case[0]
    sum = 0

    for scores in range(1, N+1) :

        sum += case[scores] 

    ave = sum/N

    count = 0

    for scores in range(1, N+1) :
        if case[scores] > ave :
            count += 1

    answer = (count/N)*100

    print(f"{answer:.3f}%")
