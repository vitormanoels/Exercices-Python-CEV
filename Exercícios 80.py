numeros = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Numero adicionado com sucesso no final da lista!')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'os valores digitados em ordem foram {numeros}')
