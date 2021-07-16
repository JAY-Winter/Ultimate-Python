#!/usr/bin/env python3v

#calculator
def calculator():
    print("6가지 기능이 탑재된 계산기입니다.")

#num1
def num1(): 
    num1 = input("첫 번째 숫자 : ")
    if num1.isdigit():
        int(num1)

    else :
        print("올바른 수를 입력하세요")  
        return calculator()

#num2
def num2():
    num2 = input("두 번째 숫자를 입력하세요 : ")
    if num2.isdigit():
        int(num2)
        return
        
    else :
        print("올바른 수를 입력하세요")  
        return calculator()

def opreator(v_num1 = num1,v_num2 = num2):
    opreator = input("연산자를 입력하세요 : ")
    if opreator =="+":
        return print(opreator(v_num1+v_num2))

    elif opreator =="-":
        return print(opreator(v_num1-v_num2))
        
    elif opreator =="*":
        return print(opreator(v_num1*v_num2)) 
        

    elif opreator =="/":
        return print(opreator(v_num1/v_num2))
        
    elif opreator =="//":
        return print(opreator(v_num1//v_num2))
        

    elif opreator =="%":
        return print(opreator(v_num1%v_num2))



calculator()
num1()
opreator()
num2()
