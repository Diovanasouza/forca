#a biblioteca random é usada para permitir operações aleatórias
import random

#foi criada uma lista de palavras padrões 
palavras = ['abacate','chocolate','paralelepipedo','goiaba']
#foram criadas variáveis que vão nos dizer as letras erradas e certas
letrasErradas = ''
letrasCertas = ''
#é uma lista dos estados do processo de enforcamento do jogador
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def cazuza():
    while True:
        x = input('Insira uma palavra: ')
        palavras.append(x)
        if x == '':
            break

#foi criada uma função principal onde a maior parte do programa irá ocorrer
def principal():
    """
    Função Princial do programa
    """
    print('F O R C A')
    cazuza()
#variável que receberá a palavra sorteada
    palavraSecreta = sortearPalavra()
#iremos utilizar depois
    palpite = ''
#chama a funçao desenhaJogo
    desenhaJogo(palavraSecreta,palpite)
#é um loop que verificará se o jogador perdeu ou ganhou o jogo,
#   analisando se o seu palpite está certo ou errado
    while True:
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():
            print('Voce Perdeu!!!')
            break
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
#é a função que será executada caso o jogador perca o jogo        
def perdeuJogo():
    global FORCAIMG
    if len(letrasErradas) == len(FORCAIMG):
        return True
    else:
        return False
#é a função que será executada caso o jogador vença o jogo
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasCertas:
            ganhou = False 
    return ganhou        
        

#é a função que recebe o palpite do jogador 
def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
#ele vai desenhar as partes visuais do programa
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
#conta a quantidade de letras erradas e certas                 
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     
#reinicia o jogo sorteando uma palavra novamente
def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()

#volta ao início(função principal)   
principal()

