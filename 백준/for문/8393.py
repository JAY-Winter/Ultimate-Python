def sum(N):

    result = N

    if N == 0 : return
    else : 
        result += N
        sum(N-1)
        return result

N = int(input())

def reduce():

    result = 0
    for i in range(N+1):
        
        result += i
    print(result)

reduce()