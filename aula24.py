# Operadores in e not in 
# Strings sao iteraveis
# 0 1 2 3 4 5
# o t a v i o 
#-6-5-4-3-2-1 
# nome = 'Otavio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome) retur False
# print('zero' not in nome) return True

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao enta em {nome}')    