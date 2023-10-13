#Estrutura de repetição while, para ficar repetindo o código
while True:
    #Try, para verificar erros nos códigos abaixo
    try:
        #Pequeno texto sobre a função do software
        print("Para calcular a área de um retângulo...")
        #Pergunta para o usuário sobre a unidade de medida que será usada
        print("Deseja o resultado em m² ou cm²?") 
        #Variável input, que define unidade de medida
        unidade = int(input("Digite 1 (m²) ou 2 (cm²)"))

        #Estrutura if else, para definir qual será a unidade de medida com base em "unidade"
        if unidade == 1:
            #Inputs que recebem medidas do retângulo
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))
            
            #Estrutura if else, que verifica se algum dos valores é zero
            if base == 0 or altura == 0:
                print("Nenhum dos valors pode ser zero!")
                area = 0
            else:
                area = base * altura
        
            #Linha que retorna valor ao usuário em m²
                
            #Função round arredonda valores, nesse caso, valor de area tem, no maximo 2 casas decimais
            print("A área do retânhgulo é: ", round(area, 2), "m²") 
            print("")
        elif unidade == 2:
            #Inputs que recebem medidas do retângulo
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))

            #Estrutura if else, que verifica se algum dos valores é zero
            if base == 0 or altura == 0:
                print("Nenum dos valors pode ser zero!")
                area = 0
            else:
                area = base * altura

            #Linha que retorna valor ao usuário em cm²
            #Função round arredonda valores, nesse caso, valor de area tem, no maximo 2 casas decimais
            print("A área do retânhgulo é: ", round(area, 2), "cm²")
            print("")
        else:
            print("Opção Inválida!")
            
    #Erro "Value", de valor, quando usuário digitar aquilo que não deveria
    except ValueError:
        print("Digite apenas valores válidos!!!")
        print("")
