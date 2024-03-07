import random

print('Seja muito bem vindo ao Guess Number da Thayna...')
numero = input('Escolha um numero:')

if numero.isdigit():
    numero = int(numero)
else:
    print('Por favor digite um numero.')
    quit()  

random_numero = random.randint(0, numero)

tentativas = 0

while True:
    numero_2 = input('Adivinhe um numero:')

    if numero_2.isdigit():
        numero_2 = int(numero_2)
    else:
        print('Por favor digite um numero.')
        continue

    tentativas = tentativas + 1

    if numero_2 == random_numero:
        print('Aceertou!')
        break
    elif numero_2 > random_numero:
        print('chutou alto! o numero é menor que isso... ')
    else:
        print('chutou baixo! o numero é maior que isso...')

print(f'numero de tentativas {tentativas}')
