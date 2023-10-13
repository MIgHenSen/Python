#Estrutura de repetição while
while True:
    #Try, para verificar erros nos códigos abaixo
    try:
        #Pequeno texto sobre a função do software
        print("Para calucular média de duas notas...")
        #Variáveis que recebem os valores das notas
        nota1 = float(input("Digite o valor da primeira nota: "))
        nota2 = float(input("Digite o valor da segunda nota: "))

        #Cálculos para o valor da média
        aux = nota1 + nota2
        media = aux/2

        #Estrutura if else, que verifica se aluno foi aprovado, reprovado ou ficará em recuperação
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
