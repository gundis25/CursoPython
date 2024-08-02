# Operador logico "not"
# Usado para inverter espressoes
# not True = False 
# not False= True
senha = input('Senha: ')

if not senha:
    print('Voce nao digitou nada')

print(not True) # False
print(not False) # True