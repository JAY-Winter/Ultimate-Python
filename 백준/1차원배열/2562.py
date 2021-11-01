# list = [3, 29, 38, 12, 57, 74, 40, 85, 61]

# for i in range( len(list)-1 ) : 

#         for j in range( point, len(list)) :

#             if max < list[point] : 

#                 max = list[point]
                

#                 break

#             else : 
#                 point += 1
#                 pass



num_list = []

for numbers in range(9) : 

    num_list.append(int(input())) 

max = num_list[0]
point = 1



for i in range( len(num_list)-1 ) : 

        for j in range( point, len(num_list)) :

            if max < num_list[point] : 

                max = num_list[point]
                

                break

            else : 
                point += 1
                pass

print(max)
print(point-1)
