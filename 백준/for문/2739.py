def multiple(N):
    
    if 2<= N <=9:
        for i in range(1,10):
            result = N*i
            
            print('{} * {} = {}'.format(N,i,result))
    else: return

multiple(N=int(input()))