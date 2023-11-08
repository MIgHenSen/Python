#Estrutura de repetição while, para ficar repetindo o código
while True:
    #Try, para verificar erros nos códigos abaixo
    try:
        print("Para calcular a área de um retângulo...")
        print("Deseja o resultado em m² ou cm²?") 
        #Variável de tipo int, que só recebe números inteiros
        unidade = int(input("Digite 1 (m²) ou 2 (cm²)"))

        #Estrutura if else, para definir qual será a unidade de medida com base em "unidade"
        if unidade == 1:
            #Inputs de tipo float, que podem receber números decimais
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))
            
            #Estrutura if else, que verifica se algum dos valores é zero
            #or("ou"), método para adicionar mais condições
            if base == 0 or altura == 0:
                print("Nenhum dos valors pode ser zero!")
                area = 0
            else:
                area = base * altura
        
            print("A área do retânhgulo é: ", round(area, 2), "m²") 
            print("")
        elif unidade == 2:
            #Inputs de tipo float, que podem receber números decimais
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))

            #Estrutura if else, que verifica se algum dos valores é zero
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
