"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número inteiro: ')
if entrada.isdigit():
      entrada_int = int(entrada)
      par_impar = entrada_int % 2 == 0
      par_impar_texto = 'ímpar'

      if par_impar:
          par_impar_texto = 'par'

      print(f'O número {entrada_int} é {par_impar_texto}')
else:
      print('Você não digitou um número inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
Hora = input('Qual a Hora atual ? ')
Hora = int(Hora)

if Hora >= 0 and Hora <=12:
     print("Bom dia")
elif Hora >= 13 and Hora <=17:
     print('Boa tarde')
elif Hora >= 18 and Hora <=23:
     print('Boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Qual seu primeiro nome? ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
     if tamanho_nome <= 4:
         print('Seu nome é muito curto!')
     elif tamanho_nome >= 5 and tamanho_nome <= 6:
         print('O seu nome é normal!')
     else:
         print('O seu nome é muito grande!')
else:
     print('Digite mais de uma letra!')
