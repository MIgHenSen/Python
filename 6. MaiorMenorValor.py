#Estrutura de repetição while
while True:
    #Try, para verificar erros nos códigos abaixo
    try:
        #Pequeno texto sobre a função do software
        print("Para saber o maior valor entre três números...")
        #Variáveis que recebem valores
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        n3 = int(input("Digite o terceiro valor: "))

        #Função max define maior valor no intervalo
        print("O maior valor é: ", max(n1, n2, n3)) #Exibe maior valor
        #Função min define menor valor no intervalo
        print("O menor valor é: ", min(n1, n2, n3)) #Exibe menor valor
        print("")

    #Erro "Value", de valor, quando usuário digitar aquilo que não deveria
    except ValueError: 
        print("Digite apenas valores válidos!!!")
        print("")
