N = int(input())

X = int(input())

def smaller(N,X):
    
    list = []
    answer = []
    
    # list 생성 for문, i>0 하므로 append(i+1)
    for i in range(N):
        list.append(i+1)

    # answer 에 X 값보다 작은 index append
    for j in range(N):
        if list[j] < X : answer.append(list[j])
    
    # list index 를 str 한 후 아래 F_answer 에서 ',' 를 없애고 출력할 예정이었음
    # for j in range(N):
    #     if list[j] < X : answer.append(str(list[j]))
    
    # F_answer = " ".join(answer)
    
    # for k in range(len(F_answer)):
        # str(F_answer[k])
    
    # print(F_answer)
    print(answer)

smaller(N,X)

# N == 10 
# 10 개의 수로 이루어진 수열
# X == 5
# 수열 중 5보다 작은 수 