def self_num():

    tmp = 1

    for i in range(10000):

        if i < 4 : 
            print(tmp)
            tmp += 2

        elif 4<=i :

            print(tmp)
            tmp += 11
            

            if tmp > 10000 :
                
                tmp - 11

                return

self_num()