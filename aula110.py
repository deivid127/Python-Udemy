# Combinations, Permutations e Product - Itertools
# Combinação - ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem Import 
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['feminino', 'masculino', 'unisex'],
    ['algodão', 'poliéster'],
]


# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
