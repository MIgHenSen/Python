while True:
    try:
        print("Para saber se um número é ímpar ou par...")
        number = int(input("Digite um número: "))

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
