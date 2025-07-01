frase = 'aaaooo'

i = 0
qtd_apareu_mais_vezes = 0
letra_apareceu_mais_vezes = ' '

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    
    qtd_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if qtd_apareu_mais_vezes < qtd_vezes_letra_apareceu_atual:
        qtd_apareu_mais_vezes = qtd_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu'
    f' {qtd_apareu_mais_vezes}x'
)