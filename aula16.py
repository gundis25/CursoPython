# if / elif       / else
# se / se nao se /se nao
entrada = input('voce quer "entrar" ou "sair"?')

if entrada == "entrar":
    print('Voce entrou no sistema')

    print('DENTRO DO IF')

elif entrada == 'sair':
    print('Voce saiu do sistema')
else:
    print('Voce digitou nem entrar nem sair.')

print('fora dos blocos')