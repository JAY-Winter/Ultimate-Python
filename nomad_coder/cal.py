#!/usr/bin/env python3v

def num1(): 
    v_num1 = input("첫 번째 숫자 : ")
    
    if type(v_num1) == str:
        int(v_num1) 
        print(type(v_num1))
    else :
        print("올바른 수를 입력하세요")  
        return calculator()
num1()

#num2
def num2():    
    # 전역변수 생성
    global v_num2 
    v_num2 = input("두 번째 숫자를 입력하세요 : ")
    if v_num2.isdigit():
        int(v_num2)
        return
        
    else :
        print("올바른 수를 입력하세요")  
        return calculator()
num2()

def opreator(n_1 = v_num1,n_2 = v_num2):

    opreator = input("연산자를 입력하세요 : ")
    if opreator =="+":
        return print(opreator(n_1+n_2))

    if opreator =="-":
        return print(opreator(n_1-n_2))
        
    if opreator =="*":
        return print(opreator(n_1*n_2)) 
        
    if opreator =="/":
        return print(opreator(n_1/n_2))
        
    if opreator =="//":
        return print(opreator(n_1//n_2))
        
    if opreator =="%":
        return print(opreator(n_1%n_2))

#calculator
def calculator():
    print("6가지 기능이 탑재된 계산기입니다.")



print(type(v_num1))