#DIFININDO NOTAS
nota_trabalho= float(input("digite sua primeira nota: "))
nota_prova=float(input("digite sua segunda nota: "))
#calculando media
media= (nota_trabalho+nota_prova)/2
print(f"a media é:{media}")
#veirificaando se aprovado ou reprovado
if media<7:
    print("REPROVADO......")
else:
    print("APROVADO.......")

