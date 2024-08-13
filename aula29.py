"""
Introduçao ao try/except
try -> tenta executar o coddigo
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobras o numero que voce digitar:')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'Odobro de {numero_str} e {numero_float * 2:.2f}')
except:
    print('Isso nao e um numero')
"""

if numero_str.isdigit(): # O numero digitado deve ser inteiro
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} e {numero_float * 2:.1f}')
else:
    print('Isso nao e um numero')
"""
