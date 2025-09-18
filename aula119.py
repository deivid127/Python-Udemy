# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Deivid')
adiciona_clientes("Joana", cliente1)
adiciona_clientes("Fernando", cliente1)
cliente1.append("Eduardo")

cliente2 = adiciona_clientes('Guilherme')
adiciona_clientes("Bruno", cliente2)

cliente3 = adiciona_clientes('Matheus')
adiciona_clientes("Maranha", cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
