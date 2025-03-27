codigo = 1234
repetir = 1

#loop para reiniciar o jogo

while repetir == 1:
    print("""
    ==> Bem vindo ao NumGuess!!! <==

    Você tem 10 tentativas para acertar um numero entre 1000 e 9999, 
    a partir da 5° tentativa o jogo começara a te ajudar com dicas.
        Boa sorte!
    """)

    TecleAlgo = input("<<<Pressione enter>>>")

    print(" ")

#variaveis para contabilizar o numero de tentativas e de tentativas restantes

    num_tentativas = 0
    tentativas_restantes = 10

#loop para receber as tentativas

    while num_tentativas < 10:
        tentativa = int(input("Digite seu palpite: "))
        
        num_tentativas += 1
        tentativas_restantes -= 1
        
        if tentativa == codigo:
            print(" --------------------------------------- ")
            print(" ")
            print(f"P A R A B E N S!\nvocê acertou!\nVocê precisou de {num_tentativas} tentativas!")
            print(" ")
            print(" --------------------------------------- ")
            repetir = int(input("Você deseja reiniciar o jogo? (Digite 1 para SIM e 0 para NÃO): "))

            break

#aviso de que o valor iserido não é valido
        
        else:
            if tentativa < 1000 or tentativa > 9999:
                print("")
                print(" --------------------------------------- ")
                print(" ")
                print(">>>ATENÇÃO!!!<<<\nO numero deve ser entre >>>1000 e 9999<<<")
                num_tentativas -= 1
                tentativas_restantes += 1
                
#operações matematicas que dividem o codigo em casas decimais e unidades
        
            else:
                codigo_1 = codigo // 1000
                codigo_2 = (codigo % 1000) // 100
                codigo_3 = (codigo % 100) // 10
                codigo_4 = codigo % 10
        
                tentativa_1 = tentativa // 1000
                tentativa_2 = (tentativa % 1000) // 100
                tentativa_3 = (tentativa % 100) // 10
                tentativa_4 = tentativa % 10
        
#comparação das casas com os codigos que permite que seja impresso na tela as casas corretas
                
                print(" ")
                print(" --------------------------------------- ")
                print(" ")
                
                if codigo_1 == tentativa_1:
                    print(codigo_1, end="")
                else:
                    print("_", end="")
        
                print(" ", end="")
        
                if codigo_2 == tentativa_2:
                    print(codigo_2, end="")
                else:
                    print("_", end="")
        
                print(" ", end="")
        
                if codigo_3 == tentativa_3:
                    print(codigo_3, end="")
                else:
                    print("_", end="")
        
                print(" ", end="")
        
                if codigo_4 == tentativa_4:
                    print(codigo_4)
                else:
                    print("_")
                    
                print(" ")
                
                if num_tentativas < 10:
                    print(f"Você errou!\nVocê ainda tem >>>{tentativas_restantes}<<< tentativas restantes")
                    print(" ")
                    print(" --------------------------------------- ")
        
                else:
                    print(f"O numero de tentativas >>>ACABARAM!<<<\nO codigo correto era >>> {codigo} <<<")
                    print(" ")
                    print(" --------------------------------------- ")
                    repetir = int(input("Você deseja reiniciar o jogo? (Digite 1 para SIM e 0 para NÃO): "))
