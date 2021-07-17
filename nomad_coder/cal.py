#!/usr/bin/env python3v

def num1(): 
    try:
        v_num1 = float(input("첫 번째 숫자 : "))
        print("float test")
    except(ValueError):
        print("올바른 숫자를 입력하세요")

def num2(): 
    try:
        v_num2 = float(input("두 번째 숫자 : "))
        print("float test")
    except(ValueError):
        return print("올바른 숫자를 입력하세요")



# def opreator(n_1 = v_num1, n_2 = v_num2):

#     opreator = input("연산자를 입력하세요 : ")
#     if opreator =="+":
#         return print(opreator(n_1+n_2))

#     if opreator =="-":
#         return print(opreator(n_1-n_2))
        
#     if opreator =="*":
#         return print(opreator(n_1*n_2)) 
        
#     if opreator =="/":
#         return print(opreator(n_1/n_2))
        
#     if opreator =="//":
#         return print(opreator(n_1//n_2))
        
#     if opreator =="%":
#         return print(opreator(n_1%n_2))

#calculator
def calculator():
    print("6가지 기능이 탑재된 계산기입니다.")
    num1()
    num2()
    opreator()


# calculator()