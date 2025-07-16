# from sys import path

# import aula101_package.modulo
# from aula101_package import modulo
# from aula101_package.modulo import *

# # from aula101_package.modulo import soma_do_modulo

# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula101_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo)
# print(variavel)
# print(nova_variavel)
# from aula101_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# fala_oi()

from aula101_package import soma_do_modulo, fala_oi
print(soma_do_modulo(2, 3))
fala_oi()