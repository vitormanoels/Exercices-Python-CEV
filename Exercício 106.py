from time import sleep
função = list()


def pyhelp():
    while True:
        função.clear()
        print('\033[0;30;42m~'*27)
        print('\033[0;30;42m  SISTEMA DE AJUDA PyHELP  ')
        print('\033[0;30;42m~'*27)
        fun = str(input('\033[mFunção ou Biblioteca > '))
        if fun == 'fim':
            sleep(0.5)
            print('\033[41m~'*20)
            print('\033[41mATÉ LOGO!')
            print('\033[41m~'*20)
            break
        função.append(fun)
        sleep(1)
        print('\033[0;30;46m~'*(40 + len(função)))
        print(f'\033[46m  Acessando o manual do comando {função} ')
        print('\033[46m~'*(40 + len(função)))
        sleep(1)
        print(f'\033[7m {fun}'.__doc__)


pyhelp()