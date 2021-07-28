# 26 

# 2 + 6 = 8 
# 68

# 6 + 8 = 14
# 84

# 8 + 4 = 12
# 42

# 4 + 2 = 6

# 26

# a =(45%10)
# print(a)

# b = (45//10)
# print(b)

import sys

N = int(input())
X = N

def cycle_plus(N,X):
        
    answer = 0

    while True :
        try : 
            tens = (N//10)
            units = (N%10)
            
            tmp = tens + units
            
            N = (units*10) + (tmp%10)
            answer += 1

            if N == X : 
                print(answer)
                break

        except : 
            print("Occured Error")
cycle_plus(N,X)

# for i in range(5):
#     tens = (N//10)
#     units = (N%10)
    
#     tmp = tens + units
    
#     N = (units*10) + (tmp%10)

#     print(N)