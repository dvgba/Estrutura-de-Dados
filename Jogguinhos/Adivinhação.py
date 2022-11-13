from random import randint 
seu_nome = input("Olá, qual o seu nome? ")
print("Okay! %s, eu escolhendo um número de 1 até 10. Você consegue adivinhar?" %seu_nome)

numAdvinhado = randint(1, 10)
numTentativas = 4

for tentativa in range(0, numTentativas):
    numEscolhido = int(input("Escolha um número: "))
    if numEscolhido == numAdvinhado:
        print("Você Acertou em %i tentativas! O numero era %i" %(numTentativas, numAdvinhado))
        break
    elif numEscolhido > numAdvinhado:
        print("Escolha um número menor")
    elif numEscolhido < numAdvinhado:
        print("Escolha um numero maior")
    else:
        print("Você não adivinhou")

print("obrigado por jogar ")

