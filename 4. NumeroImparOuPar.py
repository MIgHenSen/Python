#Estrutura de repetição while
while True:
    #Try, para verificar erros nos códigos abaixo
    try:
        #Pequeno texto sobre a função do software
        print("Para saber se um número é ímpar ou par...")
        #Variavel que recebe um numero
        number = int(input("Digite um número: "))

        #Estrutura que verifica resto da divisão de number por dois e define numeros pares ou impares
        if number % 2 == 0:
            print("É um número par")
            print("")
        else:
            print("É um número ímpar")
            print("")

    #Erro "Value", de valor, quando usuário digitar aquilo que não deveria
    except ValueError: 
        print("Números decimais não são classificados em pares ou ímpares")
        print("Digite apenas valores válidos!!!")
        print("")
