'''
História:

A empresa AWXS é um novo cliente da JWC, uma empresa especializada em desenvolvimento de soluções personalizadas. Após o sucesso da primeira fase do jogo "Número Secreto" durante a Aula 01 e aula 02, a JWC está em fase probatória para demonstrar sua competência no desenvolvimento de projetos interativos.

Agora é o momento de avançar para a Fase 3 do jogo, implementando novos desafios e funcionalidades que tornarão o jogo ainda mais interessante. Para isso, o cliente solicitou a adição de que os numeros secretos sejam criados aleatoriamente(random) e que o numero secreto esteja limitado ao intervalo entre 10-100 caso usuário digite um numero menor que 10 ou maior que 100 o jogo deve obrigar o mesmo a digitar novamente um valor entre 10 e 100.

Objetivos da Fase 3:
Pesquisar pela função random
Inplementar o randem com intervalo de 10 - 100
Configurar uma estrutura de decisão que nãp permita o jogo continuar caso o usuário tenha figitado um valor abaixo de 10 ou acima de 100 (implemente dentro do if o continue)
Entrega:
Anexar o código com as melhorias da fase 3 aqui

'''
import random
numero_secreto = random.randint(10,100)
min = 10
max = 100
contador = 0
level = 0

while True:

    level_escolhido = int(input('\nEscolha o level do game:\n1- Fácil\n2- Médio\n3- Difícil\nDigite sua escolha: '))

    if level_escolhido == 1:
        level = 30
        break        
    elif level_escolhido == 2:
        level = 15
        break        
    elif level_escolhido == 3:
        level = 5
        break       
    else:
        print("Opção inválida! Por favor, escolha um dos números disponíveis.\n")
        

while contador <= level:
    numero_escolhido = int(input('\nDigite o numero secreto entre 10 e 100: '))

    if numero_secreto == numero_escolhido:
        print('Parabéns você acertou!\n')
        break
                            
    else:
        if numero_escolhido < min or numero_escolhido > max:
            print(f'Você escolheu um númeto fora do intervalo de 10 a 100! Tentativa {contador} de {level}.\n')
            
        else:
            contador += 1
            print(f'Você errou, tente novamente! Tentativa {contador} de {level}.')
        
        

    if contador == level:
        contador += 1
        print('\nVocê excedeu o limite de tentativas. Game Over!\n')
        break