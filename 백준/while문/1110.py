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




