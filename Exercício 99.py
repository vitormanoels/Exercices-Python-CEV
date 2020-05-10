from time import sleep


def linha():
    print('-='*40)


#def maior():
#    m = 0
#    v = randint(0, 10)
#    for vl in range(0, v):
#        vl = randint(0, 10)
#        print(vl, end=' ', flush=True)
#        sleep(0.5)
#        if vl == vl:
#            vl = m
#        elif vl > m:
#            vl = m
#    print(f'Foram passados {v} valores ao todo.')
#    print(f'O maior valor encontrado foi {m}')


#maior()

#######################################################################################################
#######################################################################################################

def maior(* num):
    linha()
    print('Analizando os valores passados...')
    sleep(1)
    for c in num:
        print(c, end=' ', flush=True)
        sleep(1)
    print(f'foram informados {len(num)} valores ao todo.', flush=True)
    sleep(1)
    if len(num) > 0:
        print(f'O maior valor informado foi {max(num)}')
    elif len(num) == 0:
        print('O maior valor informado foi 0.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


###########################################################################
###########################################################################

def maior(* num):
    cont = maior = 0
    linha()
    print('Analizando os valores passados... ')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram informados {cont} valores ao todo.')
    print(f'o maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

