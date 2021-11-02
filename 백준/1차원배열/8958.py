N = int(input())

for i in range(N) :
    case = input()
    count = 0
    part_sum = 0 
    final_sum = 0

    for index in range(len(case)) :

        if case[index] == "O" :

            count += 1
            part_sum += count

            if index == len(case)-1 :
                final_sum += part_sum
            
        elif case[index] == "X" :

            final_sum += part_sum
            part_sum = 0
            count = 0


    print(final_sum)

