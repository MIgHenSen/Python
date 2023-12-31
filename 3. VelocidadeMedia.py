while True:
    try: 
        print("Para calcular a velocidade média de um automõvel...")
        print("Deseja o resultado em km/h ou em m/s?")
        print("Digite 1 (km/h) ou 2 (m/s)")
        unidade = int(input("Em que unidades quer seu resultado: "))

        if unidade == 1:
            km = float(input("Digite o valor da distância percorrida: "))
            h = float(input("Digite quanto tempo durou o percurso: "))
            speed = km / h 
            print("A velocidade desse automóvel foi, em média: ", round(speed, 2), "km/h")

            if speed > 360.0:
                print("Você foi multado por alta velocidade!")
                print("")
        elif unidade == 2:
            m = float(input("Digite o valor da distância percorrida: "))
            s = float(input("Digite quanto tempo durou o percurso: "))
            speed = m / s 
            print("A velocidade desse automóvel foi, em média: ", round(speed, 2), "m/s")

            if speed > 100.0:
                print("Você foi multado por alta velocidade!")
                print("")
        else:
            print("Opção Inválida!")
    
    #Erro "Value", de valor, quando usuário digitar aquilo que não deveria
    except ValueError: 
        print("Digite apenas valores válidos!!!")
