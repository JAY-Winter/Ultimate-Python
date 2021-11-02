remainer_list = []
dic_remainer_list = []
dic_remainer = {}
count = 1

for numbers in range(10) :

    number = int(input())

    remainer = (number % 42)
    remainer_list.append(remainer)

    dic_remainer[remainer] = count

answer = len(dic_remainer)

print(answer)
