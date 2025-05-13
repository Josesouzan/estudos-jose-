soma= 0
numero= 1
while numero !=0:
    numero = int(input("digite um número: (0 para sair)"))
    soma = soma + numero
    if numero !=0:
        print(f"a soma até o momento: {soma} ")
print(f"A soma dos números digitados é; {soma}")
