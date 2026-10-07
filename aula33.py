"""
tipos built-in,documentação, tipos imutáveis,metodos de string
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos até agora: str, int, float, bool
"""
string = "Python"
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
print(string.zfill(10))  # Preenche com zeros à esquerda até o tamanho 10