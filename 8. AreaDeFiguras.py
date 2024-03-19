while True:
    print("Para calcular área e perímetro de uma figura, escolha: ")
    print("1. Quadrado ")
    print("2. Retângulo ")
    print("3. Circulo ")

    try:
        forma = int(input("Sua escolha: "))

        if forma == 1:
            lado = float(input("Digite a medida do lado da figura: "))

            if lado == 0:
                print("Essa figura não existe!!!")
            else:
                area = lado*lado
                perim = lado*4

            print("Perímetro: ", round(perim, 2))
            print("Área: ", round(area, 2))
            print("")
        elif forma == 2:
            larg = float(input("Digite a medida da largura: "))
            comp = float(input("Digite o valor do comproiento: "))

            if larg == 0 or comp == 0:
                print("Essa figura não existe!!!")
            else:
                area = larg*comp
                perim = (larg*2) + (comp*2)

            print("Perímetro: ", round(perim, 2))
            print("Área: ", round(area, 2))
            print("")
        elif forma == 3:
            pi = 3.14
            raio = float(input("Digite a medida do lado: "))

            if raio == 0:
                print("Essa figura não existe!!!")
            else:
                area = pi* (raio**2)
                perim = 2*pi*raio

            print("Perímetro: ", round(perim, 2))
            print("Área: ", round(area, 2))
            print("")
        else:
            print("Opção Inválida!")
            print("")

    #Erro "Value", de valor, quando usuário digitar aquilo que não deveria
    except ValueError:
        print("Digite apenas valores válidos!!!")
        print("")
