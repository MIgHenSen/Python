homensComMaisDe18 = 0
mulheres = 0
#While é uma estrutura de repetição
while True:
    print("Para saber a quantidade de pessoas...")
    s = input("Digite o sexo da pessoa [M|F]")
    #Variavel que recebe apenas numeros inteiros
    idade = int(input("Digite a idade da pessoa: "))
    #Estrutura if else, para ver se é homem ou mulher
    if s.upper() == "M" and idade > 18:
        homensComMaisDe18 += 1
    if s.upper() == "F":
        mulheres += 1
        
    r = input("Deseja adicionar mais alguém [S|N]")
    if r.upper() == "N":
        print("Homens com mais de 18 anos: ", homensComMaisDe18)
        print("Numero de mulheres: ", mulheres)
        break