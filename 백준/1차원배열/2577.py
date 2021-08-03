
A = int(input())
B = int(input())
C = int(input())

N = str(A*B*C)

def N_count(N):

    list = ['0','1','2','3','4','5','6','7','8','9']

    for i in range(len(list)):

        point = list[i]
        answer = 0

        for j in range(len(N)):

            if point == N[j] : answer += 1
                
        print(answer)

N_count(N)

