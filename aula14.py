# Formatacao de strings com metododo format
a = 'A'
b = 'B'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)
'''Tudo em python e um objeto 
(Objetos geramente tem metodos detrodele Ex: .islower)
.format e um metodo
format.(a, b, c) argumentos
Parametro nomeado:
 format.(nome1=a, nome2=b, nome3=c) e um parametro nomeado e tudo que vier 
 depois dele tem que ser nomeado 
 '''