N = int(input())

X = int(input())

list = [1,10,4,9,2,3,8,5,7,6]

def smaller(N,X):

    answer = []
    
    for i in range(N):
        if list[i] < X : answer.append(list[i])

    print(answer)

smaller(N,X)

# N == 10 
# 10 개의 수로 이루어진 수열
# X == 5
# 수열 중 5보다 작은 수 