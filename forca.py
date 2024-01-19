import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    with open("palavras.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())
    
    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    erros = 0
    print(letras_acertadas)

    while("_" in letras_acertadas):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()
        if "Ç" in palavra_secreta and chute == "C":
            chute = "Ç"
        index = 0
        
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Erro! ainda restam {6 - erros} tentativas")
        
        if erros == 6:
            break
                     
        print(letras_acertadas)
        letras_faltando = letras_acertadas.count('_')
        print(f"Ainda faltam {letras_faltando} letras a serem acertadas")
        
    print("Parabéns! Você ganhou!") if "_" not in letras_acertadas else print("Fim do jogo, você perdeu.")
if(__name__ == "__main__"):
    jogar()
