a = {'A' : 90, 'B' : 80, 'C' : 70}

a_keys = list(a.keys())

for i in range(len(a)) :

    if a_keys[i] == 'B' :
        print(a.pop(a_keys[i]))


