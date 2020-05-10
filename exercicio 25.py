#nome = str(input('Qual é o seu nome completo? ')).strip().lower()
#print('Seu nome tem Silva?')
#print('silva' in nome)

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))