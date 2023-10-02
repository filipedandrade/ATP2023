import random
número = random.randint(1,100)
número_tentativas = 0
tentativa = 0

print ("QUEM É QUE ADIVINHA?")
print ("0-COMPUTADOR, 1-UTILIZADOR")
ESCOLHA = int(input("OPÇÃO: "))

if ESCOLHA == 1:
    while tentativa != número:
        tentativa = int(input("INSERE UM NÚMERO: "))
        if(tentativa<número):
            print("MAIOR")
            tentativa = tentativa + 1
        elif (tentativa>número):
            print("MENOR")
            tentativa = tentativa + 1
        

        else:
            print ("CORRECTO")
            print ("número", tentativa, "tentativa")

if ESCOLHA == 0:
    print("Pense num número")
    tentativa = 50
    vezes = 0
    N = 50
    resposta = 0
    while resposta == "maior" or resposta == "menor" or resposta == 0:
        resposta = str(input("O número que pensou é " + str(tentativa) + "?"))
        if resposta == "maior":
            tentativa = tentativa + (N/2)
        elif resposta == "menor":
            tentativa = tentativa - (N/2)
        vezes = vezes + 1
    if resposta == "acertou":
        print("Fim do jogo.")
        print (vezes)