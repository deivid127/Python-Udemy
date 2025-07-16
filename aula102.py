import copy

from dados import produtos
# Importe o módulo copy para usar a função deepcopy

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy(cópia profunda)
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in produtos            
]

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# 
# Ordene os produtos por preço crescente (do menor para o maior)
# Gere produtos_ordenados_por_preço por deep copy (cópia profunda) 