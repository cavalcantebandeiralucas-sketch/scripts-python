#Adivinhe o número secreto

import random  # radom é uma biblioteca do python que permite gerar números aleatórios. Você precisa importar a biblioteca random para poder usar a função randint() que gera um número inteiro aleatório dentro de um intervalo especificado.

secret = random.randint(1, 20)  #random. indica que você está usando a ferramenta que acabou de importar.randint(1, 20) é a função específica que escolhe um número inteiro aleatório (daí o nome random integer) entre 1 e 20.o intervalo que o computador vai escolher o numero secreto

tries = 0  # inicializa a variável tries com 0 para que o loop while funcione corretamente na primeira iteração. A variável tries é usada para contar quantas tentativas o jogador fez para adivinhar o número secreto.

guess = 0  # inicializa a variável guess com 0 para que o loop while funcione corretamente na primeira iteração.

print("I'm thinking of a number between 1 and 20")

while guess != secret:
    guess = int(input("Take a guess: "))  

    tries = tries + 1  # fazendo a contagem de tentativas, incrementando a variável tries em 1 a cada iteração do loop while.
# Give a hint using if / elif / else.
    if guess < 1 or guess > 20:
        print("That number is out of range. Try again.")
    elif guess < secret:
        print("Too low, try again.")
    elif guess > secret:
        print("Too high, try again.")
    else:            
        print("You got it in", tries, "tries!") # fornece feedback ao jogador sobre quantas tentativas ele levou para adivinhar o número secreto. A função print() exibe a mensagem "You got it in X tries!", onde X é o valor da variável tries, que representa o número de tentativas feitas pelo jogador.
