nome =input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome nao contem espaços') 

    print(f'Seu nome contem {len(nome)} letras')
    print(f'Aprimeira letra do seu nome e {nome[0]}')
    print(f'A ultima letra do seu nome e {nome[-1]}')
else:
    print('"Desculpe, voce deixou campos vazios."')
        
    

