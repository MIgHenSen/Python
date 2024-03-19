while True:
    print("----- MENU -----")
    print("1. Adição")
    print("2. Subtração")
    print("3. MUltiplicação")
    print("4. Divisão")
    print("5. Sair")

    try:
        option = int(input("Qual a sua escolha: "))
        
        if option == 5:
            print("Saindo...")
            break

        while option != 5:
            n1 = int(input("Digite o primeiro numero: "))
            n2 = int(input("Digite o segundo numero: "))
        
            if option == 1:
                print(f"{n1} + {n2} = {n1 + n2}")
                print("")
                break
            elif option == 2:
                print(f"{n1} - {n2} = {n1 - n2}")
                print("")
                break
            elif option == 3:
                print(f"{n1} * {n2} = {n1 * n2}")
                print("")
                break
            elif option == 4:
                print(f"{n1} / {n2} = {n1 / n2}")
                print("")
                break
            else:
                print("Opção Inválida!!!")

    #Erro "Value", de valor, quando usuário digitar aquilo que não deveria
    except ValueError:
        print("Digite apenas valores válidos!!!")
    #Erro "Divisão por zero", quando usuário tentar dividir por zero
    except ZeroDivisionError: 
        print("Não existem divisões por zero!!!")
