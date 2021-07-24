# `1사분면 x>0, y>0
# 2사분면 x<0, y>0
# 3사분면 x<0, y<0
# 4사분면 x>0, y<0


x,y = map(int,input().split())

if x>0 and y>0 and x != 0 and y != 0: print(1)
elif x<0 and y>0 and x != 0 and y != 0 : print(2)
elif x<0 and y<0 and x != 0 and y != 0: print(3)
elif x>0 and y<0 and x != 0 and y != 0 : print(4)
