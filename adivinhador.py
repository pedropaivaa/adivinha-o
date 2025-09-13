#modulo para gerar numero aleatorio
import random 

pensePrograma = random.randint(0,10) 
#teste para ve qual numero foi gerado
# print("O computador pensou no numero: {pensePrograma}")
usuario = int(input("Que número entre 0 e 10 o programa pensou? "))
palpites = 0

while usuario != pensePrograma:
    print("Você errou, tente novamente!")
    usuario = int(input("Digite um valor entre 0 e 10: "))
    palpites += 1

if usuario == pensePrograma:
        print("Parabéns, você acertou")
        print(f"Foram {palpites} palpite(s) até você acertar! Parabéns, você conseguiu!")
else:
        print("Que pena, voce errou")
