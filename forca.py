import random

def jogo():
    exibir_titulo()
    palavra_secreta = definir_palavra_aleatoria()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    erros = 0
    while("_" in letras_acertadas):
        chute = pede_chute(palavra_secreta)
        if chute in palavra_secreta:
            exibe_cada_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            print(f"Erro! ainda restam {6 - erros} tentativas") 
        if erros == 6:
            break
                     
        print(letras_acertadas)
        letras_faltando = letras_acertadas.count('_')
        print(f"Ainda faltam {letras_faltando} letras")

    # ternário que exibe a mensagem correta de acordo com o resultado
    print("Parabéns! Você ganhou!") if "_" not in letras_acertadas else print("Fim do jogo, você perdeu.")

def exibir_titulo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def definir_palavra_aleatoria():
    with open("palavras.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())
    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
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

if(__name__ == "__main__"):
    jogo()