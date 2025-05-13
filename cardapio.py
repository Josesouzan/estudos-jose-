opcao = int
while opcao !=5:
    print("cardápio")
    print("1- Hamburguer ")
    print("2- Pizza ")
    print("3- Salada ")
    print("4- Refrigerente ")
    print("5- Sair ")
    opcao =int(input("Ecolha uma opção: "))
    if opcao ==1:
        print("Você escolheu Hamburguer. ")
    elif opcao ==2:
        print("você escolheu Pizza. ")
    elif opcao ==3:
        print("Você escolheu salada. ")
    elif opcao ==4:
        print("Você escolheu Refrigeranteç. ")
    elif opcao ==5:
        print("saindo do cardápio.. ")
        break
    else:
        print("opção invalida. tente novamente. ")

    