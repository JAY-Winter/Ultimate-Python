import sys

# 최대 임의 값 생성
a = sys.maxsize


while a:

    A,B = map(int, sys.stdin.readline().split())

    if A==0 & B==0 : break
    else : print(A+B)
    
    
    