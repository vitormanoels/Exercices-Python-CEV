def ficha():
    n = str(input('Nome Jogador: ')).capitalize().strip()
    if n == '':
        n = '<desconhecido>'
    g = str(input('Número de Gols: '))
    if g == '':
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


ficha()

##################################################################
##################################################################


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol= g)
else:
    ficha(n, g)
