'''
História:

A empresa AWXS é um novo cliente da JWC, uma empresa especializada em desenvolvimento de soluções personalizadas. Após o sucesso da primeira fase do jogo "Número Secreto" durante a Aula 01, a JWC está em fase probatória para demonstrar sua competência no desenvolvimento de projetos interativos.

Agora é o momento de avançar para a Fase 2 do jogo, implementando novos desafios e funcionalidades que tornarão o jogo ainda mais interessante. Para isso, o cliente solicitou a adição de um sistema de níveis de dificuldade e um sistema de pontuação que premia a precisão dos jogadores.

Objetivos da Fase 2:
Implementar o sistema de níveis de dificuldade:

Fácil: O jogador tem 30 tentativas para adivinhar o número secreto.
Médio: O jogador tem 15 tentativas para adivinhar o número secreto.
Difícil: O jogador tem 5 tentativas para adivinhar o número secreto.
Implementar o sistema de pontuação:

O jogador começa com uma pontuação inicial de 100 pontos.
A cada tentativa errada, o jogador perde pontos.
O cálculo da pontuação perdida pode ser adaptado ao nível de dificuldade. Por exemplo:
Fácil: Perde 10 pontos por erro.
Médio: Perde 20 pontos por erro.
Difícil: Perde 50 pontos por erro.
Garantir que o jogador seja informado sobre sua pontuação e tentativas restantes após cada tentativa.

'''
import random
numero_secreto = random.randint(10,100)
min = 10
max = 100
contador = 0
level = 0
ponto_total = 100

while True:

    level_escolhido = int(input('\nEscolha o level do game:\n1- Fácil\n2- Médio\n3- Difícil\nDigite sua escolha: '))

    if level_escolhido == 1:
        level = 30
        ponto = 10
        break        
    elif level_escolhido == 2:
        level = 15
        ponto = 20
        break        
    elif level_escolhido == 3:
        level = 5
        ponto = 50
        break       
    else:
        print("Opção inválida! Por favor, escolha um dos números disponíveis.\n")
        

while contador <= level or ponto_total <= ponto:
        
        numero_escolhido = int(input('\nDigite o numero secreto entre 10 e 100: '))
        
        if numero_escolhido < min or numero_escolhido > max:
            print(f'Você escolheu um númeto fora do intervalo de 10 a 100! Tentativa {contador} de {level}.\n')
            #contador += 1
            ponto += ponto
            print(f'Você perdeu {ponto} de {ponto_total}')

        elif numero_secreto > numero_escolhido:
            print(f'O número secreto é maior que {numero_escolhido}! Tentativa {contador} de {level}.\n')
            contador += 1
            ponto += ponto
            print(f'Você perdeu {ponto} de {ponto_total}')

        elif numero_secreto < numero_escolhido:
            print(f'O número secreto é menor que {numero_escolhido}! Tentativa {contador} de {level}.\n')
            contador += 1
            ponto += ponto
            print(f'Você perdeu {ponto} de {ponto_total}')
            
        else:
            print(f'Parabéns você acertou! O número escolhido {numero_escolhido} é igual ao número secreto {numero_secreto}.')
            break

        if contador == level or ponto_total == ponto or ponto > ponto_total:
            contador += 1
            print('\nVocê excedeu o limite de tentativas. Game Over!\n')
            ponto += ponto
            print('\nVocê excedeu os pontos. Game Over!\n')
            break
