while True:
    try:
        print("Para calucular média de duas notas...")
        nota1 = float(input("Digite o valor da primeira nota: "))
        nota2 = float(input("Digite o valor da segunda nota: "))

        aux = nota1 + nota2
        media = aux/2

        if media > 6.0:
            print("Aprovado!!!")
            print("Sua média é: ", media)
            print("")
        elif media >= 4.0 and media <= 6.0:
            print("Ficará em Recuperação!!!")
            print("Sua média é: ", media)
            print("")
        else:
            print("Reprovado!!!")
            print("Sua média é: ", media)
            print("")

    #Erro "Value", de valor, quando usuário digitar aquilo que não deveria
    except ValueError:
        print("Digite apenas valores válidos!!!")
