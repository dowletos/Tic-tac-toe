

def printBoard(bo):
    for i in range(9):
        if i % 3==0:
            print('\r\n')
            print(f'            {bo[i]}',end='  ')
        else:
            print(f'            {bo[i]}',end='  ')




def inputNumber():
    try:

        tmp = input('\r\n\r\nПожалуйста введите значение ячейки [от 1 до 9]: ')

        x=int(tmp)
        if x not in range(1,10):
            print('         !!!!Ошибка, используйте только цифры от 1 до 9!!!!!')
            return inputNumber()
        else:
            inputNumber=x
            return x
    except ValueError:
        return inputNumber()

def putSign(sign):
    if (sign % 2) ==0:
        return "O"
    else:
        return "X"

def checkWinner(bo):
    pattern=([1,2,3],
             [4,5,6],
             [7,8,9],
             [1,4,7],
             [2,5,8],
             [3,6,9],
             [1,5,9],
             [3,5,7])
    xCur=0
    for xSign in ['O', 'X']:
        for y in pattern:
            for x in range(3):
                if bo[y[x]-1]==xSign:
                    xCur+=1
            if xCur==3:
                STOP_GAME = False
                print(f'|----------------{xSign} ПОБЕДИТЕЛЬ!!!----------------|')
                printBoard(bo)
                return True



            else:
                xCur=0






def main(slogan):
    STOP_GAME = True
    print(slogan)
    bo=['_','_','_','_','_','_','_','_','_']
    printBoard(bo)
    c=0;
    while STOP_GAME:

        c+=1
        val=inputNumber()
        if bo[val-1]=='_':
            bo[val-1]=putSign(c)
            if checkWinner(bo):
                STOP_GAME=False
                break
            printBoard(bo)
        elif STOP_GAME==False:
            break
        else:
            print('|----------------Выбранная вами ячейка уже занята. Пожалуйста попробуйте другую ячейку!----------------|')
            printBoard(bo)
            continue


if __name__ == '__main__':
    main('              Welcome to GAME             ')


