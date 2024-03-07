print('Seja bem vindo ao quiz da Thayna!')
pergunta = input('Quer começar? (s/n)')

if pergunta != 's':
    quit()

score = 0 

print('Começando...')
print('Quem desenvolveu o jogo GTA? \n (a) Rockstar games \n (b) Ubisoft \n (c) Activision \n (d) EA \n')
resposta_1 = input('Qual alternativa correta: ')

if resposta_1 == 'a':
    print('correto!')
    score = score + 1
else:
    print('incorreto... resposta certa é letra (a)')

print('Qual o nome do protagonista de hunterxhunter?\n (a)killua \n (b)gon \n (c)hisoka')
resposta_2 = input('Qual alternativa correta: ')

if resposta_2 == 'b':
    print('Correto!')
    score = score + 1
else:
    print('incorreto... resposta certa é letra (b)')

print(f'Quiz acabou... Pontuaçao:{score}')