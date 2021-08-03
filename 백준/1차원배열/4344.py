import sys

C = int(input())

def over_ave(C):

    answer = []

    for i in range(C):

        score = list(map(int, sys.stdin.readline().split()))
        N  = score[0]
        ave = (sum(score)-N)/N
        count = 0


        for j in range(N+1):

            if score[j] > ave : 
                count += 1

            over_students_ave = (count/N)*100            
            round(over_students_ave)

            
        answer.append("%0.3f" %+over_students_ave+"%")

    for k in range(len(answer)):

        print(answer[k])

over_ave(C)



