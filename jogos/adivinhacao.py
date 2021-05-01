import random

def jogar():

    print("*********************************")
    print("Bem vindo no jogo de Adivinhação")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    limite_de_tentaivas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        limite_de_tentaivas = 20
    elif nivel == 2:
        limite_de_tentaivas = 10
    else:
        limite_de_tentaivas = 5

    for total_de_tentativas in range(0, limite_de_tentaivas, 1):
        tentativas_restantes = limite_de_tentaivas - total_de_tentativas

        print("Você possui %d tentativa(s) restantes" % tentativas_restantes)

        chute = int(input("Digite o seu número entre 1 e 100: "))
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto

        if acertou:
            print("Você acertou e fez %d pontos" % pontos)
            break
        else:
            dica = "maior" if maior else "menor"
            print("Você errou! O seu chute foi %s do que o número secreto" % dica)
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    if not acertou:
        print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

    print("Fim do jogo")

if __name__ == "__main__":
    jogar()
