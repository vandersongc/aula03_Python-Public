numero_secreto = 8

while True:
        
        numero_escolhido = int(input('Digite o numero secreto: '))

        if numero_escolhido != numero_secreto:
            print('Número errado. ')
            resposta = input('Você deseja tentar novamente?(S/N)')
            if resposta == 'N':
                break
                    
        else:
            print('Parabéns! Você acertou o número secreto!')