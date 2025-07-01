"""
Closure e funções que retornam outras funções
"""
import os

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

# nome = input('Digite seu nome:')

# os.system('cls')

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))


