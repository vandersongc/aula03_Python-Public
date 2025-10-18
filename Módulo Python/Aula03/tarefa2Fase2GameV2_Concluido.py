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
numero_secreto = 8
contador = 0
level = 0

while True:

    level_escolhido = int(input('Escolha o level do game:\n1- Fácil\n2- Médio\n3- Difícil\nDigite sua escolha: '))

    if level_escolhido == 1:
        level = 5 #30
        break        
    elif level_escolhido == 2:
        level = 4 #15
        break        
    elif level_escolhido == 3:
        level = 3 #5
        break       
    else:
        print("\nOpção inválida! Por favor, escolha um dos números disponíveis.\n")
        

while contador <= level:
    numero_escolhido = int(input('Digite o numero secreto: '))

    if numero_escolhido == numero_secreto:
        print('Parabéns você acertou!')
        break
                            
    else:
        contador += 1
        print(f'Você errou, tente novamente! Tentativa {contador} de {level}.')
        

    if contador == level:
        contador += 1
        print('Você excedeu o limite de tentativas. Game Over!')
        break