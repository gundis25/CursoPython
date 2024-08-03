"""
Interpolaçao basica de strings
s - string
d e i - int
f - float
.<numero de digitos>f
x e X - Hexadecimal (ABCDEF0123456789)
(Caractere)<> ^)(quantidade)
> - Escquerda
< - Direita
 ^ - Centro
 = - Forca o numero a aparecer ante do zeros
 sinal - + ou -
 Ex. 0>-100,.1f
 Conversion flags - !r !s !
"""
variavel ='ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'Ohexadecimal de 1500 e {1500:08X}')
print(f'{variavel!r}')
