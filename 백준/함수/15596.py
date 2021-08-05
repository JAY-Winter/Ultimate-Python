
n = int(input())

def sum(n):

    a = []
    answer= 0

    for i in range(n):
        a.append(i+1)
        
    for j in range(len(a)):
        answer += a[j]
    
    return print(answer)
    
sum(n)