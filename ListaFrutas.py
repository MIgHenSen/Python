while True:
    #Criação de uma lista
    list = ["maçã", "banana", "morango", "melancia", "pêra"]
    print("Tenho uma lista de 5 frutas em meu sistema, adivinhe quais são")
    print("Você terá 5 chances, vamos ver quantas você acertará: ")
    #Variável que define quantidade de acertos
    acertos = 0
    #for é um outro laço de repetição
    for numero in range(0, 5):
        fruta = input("Digite o nome de uma fruta, tudo em letras minúsculas, por favor: ")
        if fruta in list:
            print("Parabéns, ", fruta, "está na minha lista")
            acertos = acertos + 1
            print("")
        else:
            print("Não, ", fruta, "não está na minha lista")
            print("")
    print("Parabéns, você acertou ", acertos, "frutas")
    print("Teste sua sorte, desafie outra pessoa a tentar")
    print("")
    print("")
