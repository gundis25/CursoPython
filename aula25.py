"""
Interpolaçao basica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 10009.5897643
variavel = '%s, o preço e R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d e %08X' % (1500,1500))
