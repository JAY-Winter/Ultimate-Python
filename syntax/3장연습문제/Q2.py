
sum = 0
n = 1

while True :

    if n%3 == 0 :
        sum += n
        n += 1
        # print(sum)

    elif n == 1000 : break

    else : n += 1


print(sum)