def multiple(A,B):
    global A_list
    global B_list
    A_list = []
    B_list = []

    for i in range(3):

        A_list.append(A%10)
        A = A//10

        B_list.append(B%10)
        B = B//10

A,B = map(int, input().split(','))

multiple(A,B)


fir = A*B_list[0]
sec = A*B_list[1]
thr = A*B_list[2]

print(fir)
print(sec)
print(thr)