x_list = [1,2,3,4,5,6,7,8,9,10]

y_list = [2,3,4,5,6,7,8,9,10,11]

case = [x*y for x in x_list
            for y in y_list]

print(case)