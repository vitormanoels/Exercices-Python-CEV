from datetime import date


def voto():
    ano = date.today().year
    print('___' * 10)
    nas = int(input('Em que ano você nasceu? '))
    idade = ano - nas
    print(f'Com {idade} anos:', end=' ')
    if idade < 16:
        #n = 'NÃO VOTA.'
        #return n
        print('Não vota.')
    elif 16 <= idade < 18 or idade >= 60:
        #op = 'VOTO OPCIONAL.'
        #return op
        print('Voto opcional.')
    elif 18 <= idade < 60:
        #ob = 'VOTO OBRIGATÓRIO.'
        #return ob
        print('Voto obrigatório.')


voto()

#######################################################
#######################################################


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
