from operator import index

def jogar():    
    print("******************")
    print("Bem vindo ao jogo da Forca!!!")
    print("*****************")
    
    palavra_secreta = 'Corinthians'   
    enforcou = False
    acertou = False
    
    tamanho_da_palavra = len(palavra_secreta)
    
    print("A palavra secreta tem {} letras.".format(tamanho_da_palavra))
    
    while(not enforcou and not acertou):
        chute = input("Informe uma letra:  ")
        chute = chute.strip()
        
        index=0
        for letra in palavra_secreta:
            if (chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra , index))
            index = index + 1       
        print("jogando...")
        
    print("fim do jogo")

if(__name__ == '__main__' ):
    jogar()