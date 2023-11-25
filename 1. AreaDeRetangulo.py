while True:
    try:
        print("Para calcular a área de um retângulo...")
        print("Deseja o resultado em m² ou cm²?") 
        unidade = int(input("Digite 1 (m²) ou 2 (cm²)"))

        if unidade == 1:
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))
            
            if base == 0 or altura == 0:
                print("Nenhum dos valors pode ser zero!")
                area = 0
            else:
                area = base * altura
        
            print("A área do retânhgulo é: ", round(area, 2), "m²") 
            print("")
        elif unidade == 2:
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))

            if base == 0 or altura == 0:
                print("Nenum dos valors pode ser zero!")
                area = 0
            else:
                area = base * altura

            print("A área do retânhgulo é: ", round(area, 2), "cm²")
            print("")
        else:
            print("Opção Inválida!")
            
    #Erro "Value", de valor, quando usuário digitar aquilo que não deveria
    except ValueError:
        print("Digite apenas valores válidos!!!")
        print("")
