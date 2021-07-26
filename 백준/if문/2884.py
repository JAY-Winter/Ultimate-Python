

H, M = map(int,input().split())

if 59 >= M >= 45 : 
    alarm_M = int(M-45)
    print(H, alarm_M)
#45 분 미만일 때
elif H==0 :
    alarm_H2 = 23
    alarm_M3 = int(M+15)
    print(alarm_H2, alarm_M3)
else :
    alarm_H = int(H-1)
    alarm_M2 = int(M+15)
    print(alarm_H, alarm_M2)


# 10 10 -> 9 25
# 0 30 -> 23 45
# 23 40 -> 22 55


# 0<= H <=23
# 0<= M <= 59



# 10분일 때 -10 한 뒤 60에서 남은값을 뺌 
# 그리고 H -1 





