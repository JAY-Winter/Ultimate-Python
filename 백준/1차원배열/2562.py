num_list = []
max = 0

for i in range(9) :

    num = int(input())
    num_list.append(num)


    if max < num_list[i] : 
        max = num_list[i]
        index = i

print(max)
print(index+1)


