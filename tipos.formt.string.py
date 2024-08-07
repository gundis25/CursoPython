nome = 'Marcos'
idade = 43
altura = 1.69
# F-string
mensagem = f'Ola , meu nome é {nome}, tenho {idade} anos e minha altura é {altura} metros.'
print(mensagem)

# format()
mesma_mensagem = 'Ola , meu nome é {}, tenho {} anos e minha altura é {} metros.'.format(nome, idade, altura)
print(mesma_mensagem)

#Interpolação %
mesma_mensagem = 'Ola , meu nome é %s, tenho %d anos e minha altura é %.2f metros.'% (nome, idade, altura)
print(mesma_mensagem)