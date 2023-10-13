#Estrutura de repetição while
while True:
    #Try, para verificar erros nos códigos abaixo
    try: 
        #Pequeno texto sobre a função do software
        print("Para calcular a velocidade média de um automõvel...")
        #Pergunta para o usuário sobre a unidade de medida que será usada
        print("Deseja o resultado em km/h ou em m/s?")
        print("Digite 1 (km/h) ou 2 (m/s)")
        #Input que define unidade de medida
        unidade = int(input("Em que unidades quer seu resultado: "))

        #Estrutura if else, que define valores baseada em "unidade"
        if unidade == 1:
            #Variáveis que recebem dados para as informações
            km = float(input("Digite o valor da distância percorrida: "))
            h = float(input("Digite quanto tempo durou o percurso: "))
            #Variavel que define valor da velocidade
            speed = km / h 
            #Exibindo valores ao usuário em km/h
            print("A velocidade desse automóvel foi, em média: ", round(speed, 2), "km/h")

            #Estrutura if else que diz ao usuário se ele foi multado ou não
            if speed > 360.0:
                print("Você foi multado por alta velocidade!")
                print("")
        elif unidade == 2:
            #Variáveis que recebem dados para as informações
            m = float(input("Digite o valor da distância percorrida: "))
            s = float(input("Digite quanto tempo durou o percurso: "))
            #Variavel que define valor da velocidade
            speed = m / s 
            #Exibe valores ao usuário na unidade m/s
            print("A velocidade desse automóvel foi, em média: ", round(speed, 2), "m/s")

            #Estrutura if else que diz ao usuário se ele foi multado ou não
            if speed > 100.0:
                print("Você foi multado por alta velocidade!")
                print("")
        else:
            print("Opção Inválida!")
    
    #Erro "Value", de valor, quando usuário digitar aquilo que não deveria
    except ValueError: 
        print("Digite apenas valores válidos!!!")
