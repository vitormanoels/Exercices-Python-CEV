#cidade = str(input('Qual cidade você mora?')).lower().strip()
#print('Atualizando cidade...')
#print('O nome da sua cidade {} começa com Santo'.format('santo' in cidade))

cid = str(input('Em que cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')