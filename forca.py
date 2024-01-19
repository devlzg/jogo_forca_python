import random

def jogo():
    exibir_titulo()
    palavra_secreta = definir_palavra_aleatoria("palavras.txt")
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    erros = 0
    while("_" in letras_acertadas):
        chute = pede_chute(palavra_secreta)
        if chute in palavra_secreta:
            exibe_cada_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca()
        if erros == 7:
            break
                     
        print(letras_acertadas)
        letras_faltando = letras_acertadas.count('_')
        print(f"Ainda faltam {letras_faltando} letras")

    # ternário que exibe a mensagem correta de acordo com o resultado
    if "_" not in letras_acertadas:
        imprimir_mensagem_vencedor()
    else:
        imprimir_mensagem_perdedor()

def exibir_titulo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def definir_palavra_aleatoria(nome_arquivo = "palavras.txt", primeira_linha = 0):
    with open(nome_arquivo, "r") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())
    palavra_secreta = palavras[random.randrange(primeira_linha, len(palavras))].upper()
    return palavra_secreta

def inicializar_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute(palavra_secreta): 
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    if "Ç" in palavra_secreta and chute == "C":
        chute = "Ç"
    return chute

def exibe_cada_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def imprimir_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprimir_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print(f"Erro! ainda restam {6 - erros} tentativas") 
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogo()