from time import sleep


def linha():
    print('-='*20)


def contagem(a, b, c):
    if a > b:
        if c == 0:
            c = 1
        elif c < 0:
            c = - c
        for g in range(a, b - 1, -c):
            print(g, end=' ', flush=True)
            sleep(0.5)
    elif b > a:
        if c == 0:
            c = 1
        elif c < 0:
            c = -c
        for g in range(a, b + 1, c):
            print(g, end=' ', flush=True)
            sleep(0.5)
    print('FIM!')


linha()
print('Contagem de 1 até 10 de 1 em 1')
contagem(1, 10, 1)
linha()
print('Contagem de 10 até 0 de 2 em 2')
contagem(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
d = int(input('Início: '))
e = int(input('Fim: '))
f = int(input('Passo: '))
linha()
print(f'Contagem de {d} até {e} de {f} em {f}')
contagem(d, e, f)
linha()
print()
linha()
print()
linha()


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar!')
ini = int(input('Início:  '))
fin = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fin, pas)
