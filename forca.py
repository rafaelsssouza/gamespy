import random


def jogar():
    print("******************")
    print("Bem vindo ao jogo da forca")
    print("*****************")
    
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close()    
    
    numero = random.randrange(0, len(palavras))
    
    palavra_secreta = palavras[numero].upper()
    
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0
    
    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        
        chute = input("Me diga uma letra: ")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1 
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(len(palavra_secreta)-erros))
        
        enforcou = (erros == len(palavra_secreta))
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
    if(acertou):
        print("Voce ganhou !!")
    else:
        print("Voce se enforcou !!")
        
    print("Fim do jogo")    
    
if(__name__ == '__main__'):
    jogar()