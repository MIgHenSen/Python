lista = []
media = 0

#Função para adicionar nota à lista
def adicionarNota(nota):
    lista.append(nota)
  
#Função para calcular e exibir média
def media():
    media = sum(lista) / len(lista)
    print("Sua media foi de: ", media)
    
#Laço de repetição while
while True:
    #Input que pode receber número decimal
    nota = float(input("Digite uma nota: "))
    adicionarNota(nota)
    p = input("Deseja adicionar uma nota à lista? [N|S] ")
  
    #Método upper deixa letras digitadas em caixa alta
    if p.upper() == "N":
        media()
        #break finalisa o programa
        break