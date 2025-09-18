# Exercício - Lista de tarefas cokm desfazer e refazer
# Música pra codar =)
# Everbody wants to rule the world - Tears for fears
# todo = [] --> lista de tarefas
# todo = ['fazer café'] --> adicionar fazer café
# todo = ['fazer café', 'caminhar'] --> adicionar caminhar
# desfazer = ['fazer café'] --> Refazer ['caminhar']
# desfazer = [] --> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa=} removida com sucesso')
    tarefas_refazer.append(tarefa)
    print()



def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print()



def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa')
        return
    print(f'{tarefa=} adicionada com sucesso')
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []


while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    else:
        adicionar(tarefa, tarefas)
        continue