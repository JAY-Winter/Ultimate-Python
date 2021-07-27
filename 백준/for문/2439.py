

# # N == 5
# for i in range(N):
#     count = N-i
#     print(f"%{count}s" %"*"*(i+1))



# print("%4s" %"*")
# print("%3s" %"**")
# print("%2s" %"***")
# print("%1s" %"****")
# print("%0s" %"*****")


N = int(input())
for j in range(N):
    print(' '*(N-j-1)+'*'*(j+1))