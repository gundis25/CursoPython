nome = input('Qual o seu nome? ')
print(f'O seu nme e {nome=}')

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro umero: ')

print(f'A soma dos numeros e: {numero_1 + numero_2}') 
#concatencao pois avariavel e do tipo str.

numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro umero: '))

print(f'A soma dos numeros e: {numero_1 + numero_2}')
# Type casting coersao de tipo que funciona mas pode gerar erro.

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro umero: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos numeros e: {int_numero_1 + int_numero_2}')
# desta forma o codigo pode quebrar porem e posivel fazer uma checagem 
#antes da quebra o codigo