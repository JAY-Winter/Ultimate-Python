def plus():
    N = int(input())

    # N이 입력되면
    # A,B 를 N번 입력후
    # return A+B

    while N !=0 :
        A,B = map(int,input().split())
        result_plus = A+B

        print(result_plus)
        N = N-1
        
        if N==0 : return

plus()