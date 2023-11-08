#Estrutura de repetição while
while True:
    #Try, para verificar erros nos códigos abaixo
    try:
        print("Para clacular equações de 2° grau: ")
        #Variaveis que podem receber numeros decimais
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
    
        D = (b**2 - 4*a*c)
        x1 = (-b + D**(1/2)) / (2*a)
        x2 = (-b - D**(1/2)) / (2*a)

        print('Valor de x1: {0}'.format(x1))
        print('Valor de x2: {0}'.format(x2))
        print("")
        
    #Erro "Value", de valor, quando usuário digitar aquilo que não deveria
    except ValueError:
        print("Digite apenas valores válidos!")
        print("")
