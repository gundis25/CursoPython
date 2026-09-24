"""
Fatiamento de strings
 012345678
 Ola mundo
-987654321
Fatiamento [i:f:p] [::]
obs. : a funçao len retorna a qtd
de caracteres da str
"""
variavel = "Ola mundo"
print(variavel[4])#pega o  caractere da posiçao 4
print(variavel[4:9])#pega os caracteres da posiçao 4 até 9
print(variavel[4:8])#pega os caracteres da posiçao 4 até 8
print(variavel[:5])#pega os caracteres da posiçao 0 até 5
print(variavel[5:])#pega os caracteres da posiçao 5
print(variavel[-8:-2])#pega os caracteres da posiçao -8 até -2
print(variavel[3])#pega o caractere da posiçao 3
print(variavel[4])#pega o caractere da posiçao 4
print(len(variavel[3]))#pega o tamanho da string na posiçao 3
print(len(variavel))#pega o tamanho da string
print(variavel[4])#pega o caractere da posiçao 4
print(variavel[0:len(variavel):1])#pega os caracteres da posiçao 0 até o tamanho da string de 1 em 1
print(variavel[0:9:2])#pega os caracteres da posiçao 0 até 9 de 2 em 2
print(variavel[-1:-10:-1])#pega os caracteres da posiçao -1 até -10 de um em um