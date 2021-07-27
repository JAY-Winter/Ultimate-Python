def multiple(A,B):

    A_list = []
    B_list = []

    for i in range(3):

        A_list.append(A%10)
        A = A//10

        B_list.append(B%10)
        B = B//10






A,B = map(int, input().split(','))
# A = 472, B = 385
N =  int(3)

def mul(A,B,N):

    A_list = [] 
    B_list = []

    if A == 0 and B == 0 : return print(A_list,B_list)
    else :
        A_list.append(A%10)
        A = A//10

        B_list.append(B%10)
        B = B//10



mul(A,B,N)