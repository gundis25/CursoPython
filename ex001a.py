"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Digite um numero:')
if entrada.isdigit():
  int_entrada = int(entrada)
  par_ou_impar = int_entrada % 2 == 0
  if par_ou_impar:
    print(f'O número{int_entrada} é par')
  else:
    print(f'O número{int_entrada} é impar')
else:
  print('Entrada incorreta por favor digite um número.')


try:
  int_entrada = int(entrada)
  par_ou_impar = int_entrada % 2 == 0
  if par_ou_impar:
    print(f'O número {int_entrada} é par')
  else:
    print(f'O número {int_entrada} é impar')
except:
  print('Entrada invalida, digite um numero inteiro')



