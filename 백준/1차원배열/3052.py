
list = []
answer= 1

for i in range(10):
    N = int(input())
    list.append(N)

for j in range(10):
    
    x = list[j]%42

    for k in range(9):

        y = list[k+1]%42

    if x != y : answer += 1
    # elif x == y : answer -= 1
print(answer)

