def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_",]
    
    
    enforcou = False
    acertou = False
    erros = 0
    
    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()
        index = 0
        
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        
        acertou = "_" not in letras_acertadas
                
        print(letras_acertadas)
        letras_faltando = letras_acertadas.count('_')
        print(f"Ainda faltam {letras_faltando} letras a serem acertadas")
        
    print("Parabéns! Você ganhou!") if acertou else print("Fim do jogo, você perdeu.")
if(__name__ == "__main__"):
    jogar()
