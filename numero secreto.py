#declarar variaveis
import random
numero_secreto= random.randint (1,10)
tentativas =0
contagem_tentativas =0
print("BEM- VIDO AO JOGO DO NÚMERO SECRETO..")
print("TENTE ADIVINHAR O NÚMERO SECRETO: ")
#laço de repetição
while tentativas != numero_secreto:
    numero= int(input("digite um numero: "))
    contagem_tentativas=contagem_tentativas+1
    if numero ==numero_secreto:
        print("parabens você acertou o numero secrreto. ")
        print(f"você precisou de {contagem_tentativas} para acertar. ")
        break
    elif numero < numero_secreto:
        print("o número secreto e maior. ")
    else :
        print("o número secreto é menor.")
        