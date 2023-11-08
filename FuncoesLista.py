lista = []

#Função para exibir lista
def exibeLista():
    print(lista)
    
#Função para adicionar itens na lista
def adicionarItem(palavra):
    lista.append(palavra)
    
#Função para exibir cada posição em uma linha diferente
def palavraPorPalavra():
    for x in lista:
        print(x)
        
#Função para excluir todos os itens da lista
def limparLista():
    lista.clear()
    
#Função para exibir posição específica da lista
def posicaoEspecifica(x):
    print(lista[x])
    
#Função para substituir posição da lista
def substituirPosicao(x, palavra):
    lista[x] = palavra
    
##Função para excluir última posição
def excluirUltimaPosicao():
    lista.pop()
    
#Função para adicionar item em posição epecífica
def adicionarPosicaoEspecifica(x, palavra):
    lista.insert(x, palavra)
    
#Função para deletar posição específica
def deletarPosicaoEspecifica(x):
    del lista[x]
    
print("Em meu sistema tenho uma lista vazia e você pode fazer algumas coisas com ela:")
print("")

#Estrutura while
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
    
    #Try, para verificar erros nos códigos abaixo
    try:
        #Input que recebe numero inteiro
        option = int(input("Sua Escolha: "))
        
        #Estrutura if else, para se o usuário quiser finalizar o programa
        if option == 9:
            print("Saindo...")
            break
        
        #Estrutura while, para repetir enquanto option for dierente de 9
        while option != 9:
            #Estrutura if else, que trata as escolhas do usuário
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