list = []
ans_list = []

div = 42

for i in range(10) : 

    list.append(int(input()))

    ans = list[i]%42

    ans_list.append(ans)

count = 0 

for i in range(9) :

    for j in range(i+1, 10) :

        if ans_list[i] == ans_list[j] :

            count += 1
        
        
if count == 0 : 
    answer = 1

elif 

else : 
    answer = 10 - count


print(answer)