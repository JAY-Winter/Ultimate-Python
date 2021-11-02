N = int(input())

ans_score_list = list(map(int, input().split()))

M = ans_score_list[0]

for score in ans_score_list :

    if M < score : M = score

sum = 0

for j in range(N) :

    new_score = ans_score_list[j]/M*100
    sum += new_score

ave = sum/N

print(ave)
