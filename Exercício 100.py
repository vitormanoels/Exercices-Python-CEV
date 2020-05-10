from random import randint
from time import sleep
numeros = []


def sorteia():
    for c in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)
    print(f'Sorteado 5 valores da lista: ', end='')
    for v in numeros:
        print(v, end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapar():
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia()
somapar()

#############################################################################
#############################################################################


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.2)
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os valores pares de {lista}, temos {soma}')


numeross = list()
sorteia(numeross)
somapar(numeross)
