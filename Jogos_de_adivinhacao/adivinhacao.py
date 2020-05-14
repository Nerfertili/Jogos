print("\n""ola gabriel, bem vindo ao jogo de adivinhação\n")

numero_secreto = 18

chute = int(input("digite o numero que voce deseja churtar:"))
print("\nvoce chutor esse numero:",chute,"\n")
if( chute == numero_secreto ):
    print("parabens! voce acertou :)")
else:
    print("voce errou :(")