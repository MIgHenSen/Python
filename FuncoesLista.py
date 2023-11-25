lista = []
def exibeLista():
    print(lista)
def adicionarItem(palavra):
    lista.append(palavra)
def palavraPorPalavra():
    for x in lista:
        print(x)
def limparLista():
    lista.clear()
def posicaoEspecifica(x):
    print(lista[x])
def substituirPosicao(x, palavra):
    lista[x] = palavra
def excluirUltimaPosicao():
    lista.pop()
def adicionarPosicaoEspecifica(x, palavra):
    lista.insert(x, palavra)
def deletarPosicaoEspecifica(x):
    del lista[x]
    
print("Em meu sistema tenho uma lista vazia e você pode fazer algumas coisas com ela:")
print("")

while True:
    print("----- MENU -----")
    print("1. Adicionar palavra")
    print("2. Limpar lista")
    print("3. Exibir Lista")
    print("4. Exibir posição específica")
    print("5. Substituir posição na lista")
    print("6. Excluir ultima posição da lista")
    print("7. Adicionar palavra em posição especifica")
    print("8. Deletar posição")
    print("9. Finalisar Programa")
    
    try:
        option = int(input("Sua Escolha: "))
        
        if option == 9:
            print("Saindo...")
            break
        
        while option != 9:
            if option == 1:
                palavra = input("\nDigite uma palavra: ")
                adicionarItem(palavra)
                exibeLista()
                print("")
                break
            if option == 2:
                limparLista()
                exibeLista()
                print("")
                break
            if option == 3:
                print("As palavras que estão na lista são:")
                palavraPorPalavra()
                print("")
                break
            if option == 4:
                print("As posições começam em zero")
                x = int(input("\nQual posição quer ver: "))
                posicaoEspecifica(x)
                print("")
                break
            if option == 5:
                exibeLista()
                print("As posições começam em zero")
                x = int(input("\nQual posição quer substituir: "))
                palavra = input("\nQual a nova palavra: ")
                substituirPosicao(x, palavra)
                print("Nova lista: ", exibeLista())
                print("")
                break
            if option == 6:
                excluirUltimaPosicao()
                break
            if option == 7:
                exibeLista()
                print("As posições começam em zero")
                x = int(input("\nQual posição será alterada: "))
                palavra = input("\nQual a nova palavra: ")
                adicionarPosicaoEspecifica(x, palavra)
                exibeLista()
                break
            if option == 8:
                exibeLista()
                print("As posições começam em zero")
                x = int(input("\nQual posição será deletada: "))
                deletarPosicaoEspecifica(x)
            else:
                print("Opção Inválida!")
                
    #Erro "Value", de valor, quando usuário digitar aquilo que não deveria
    except ValueError:
        print("Digite apenas valores válidos, por favor")
