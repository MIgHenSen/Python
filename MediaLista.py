lista = []
media = 0

def adicionarNota(nota):
    lista.append(nota)
def media():
    media = sum(lista) / len(lista)
    print("Sua media foi de: ", media)
    
while True:
    nota = float(input("Digite uma nota: "))
    adicionarNota(nota)
    p = input("Deseja adicionar uma nota à lista? [N|S] ")
  
    if p.upper() == "N":
        media()
        #break finalisa o programa
        break
