homensComMaisDe18 = 0
mulheres = 0
while True:
    print("Para saber a quantidade de pessoas...")
    s = input("Digite o sexo da pessoa [M|F]")
    idade = int(input("Digite a idade da pessoa: "))
    if s.upper() == "M" and idade > 18:
        homensComMaisDe18 += 1
    if s.upper() == "F":
        mulheres += 1
        
    r = input("Deseja adicionar mais alguém [S|N]")
    if r.upper() == "N":
        print("Número de Homens: ", homensComMaisDe18)
        print("Numero de Mulheres: ", mulheres)
        break

