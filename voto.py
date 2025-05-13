ano_atual= 2025
ano_de_nascimento= int(input("digite seu ano de nascimento: "))
idade= ano_atual- ano_de_nascimento
print(f"você tem {idade} anos")
if idade <16:
    print ("você não pode votar. ")
elif idade <18 or idade >70:
    print("seu voto e facultativo. ")
elif idade >=18 and idade <=70:
    print("seu voto é obrigatório. ")
