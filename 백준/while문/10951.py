import sys

def EOF():

    while True:
        try :
            A,B = map(int, sys.stdin.readline().split())

            print(A+B)

        except :
            # print('Occured Error')
            exit()

EOF()