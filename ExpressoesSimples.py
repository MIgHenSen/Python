while True:
    try:
        print("Para calcular espressões matemáticas simples...")
        conta = input("Digite a expressão: ")
        
        resultado = eval(conta)
        print("Resultado: ", resultado)
        print("")
        
    #NameError ocorre quando um valor digitado não existe
    except NameError:
        print("Digite apenas expressões, por favor!")
