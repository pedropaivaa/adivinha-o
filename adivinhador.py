#modulo para gerar numero aleatorio
import random 

pensePrograma = random.randint(0, 100)
#teste para ve qual numero foi gerado
# print("O computador pensou no numero: {pensePrograma}")
usuario = int(input("Que numero entre 0 e 199 o programou pensou?: "))


if usuario == pensePrograma:
    print("Parabens, você acertou!")
else:
    print("Que pena, você errou!")
