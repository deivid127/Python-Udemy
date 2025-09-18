import json

pessoa = {
    'nome': 'Deivid',
    'sobrenome': 'Leite',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.72,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula118.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
        )
print('Arquivo JSON criado!')

# with open('aula118.json', 'r', encoding='utf8') as arquivo:
#     pessoa = json.load(arquivo)
#     # print(pessoa)
#     # print(type(pessoa))
#     print(pessoa['nome'])
