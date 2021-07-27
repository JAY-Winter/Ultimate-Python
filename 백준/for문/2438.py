def star(N):

    if N==0 : return
    else : 
        star(N-1)
        print('*'*N)
        
N = int(input())
star(N)