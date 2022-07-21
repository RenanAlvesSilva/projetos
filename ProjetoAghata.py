from time import sleep
from datetime import date
from random import randint
atual = date.today().year
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Vamos começar com algumas questões.\n')
print('Para podermos início, preciso que você acerte nossa data de início de namoro.')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
print('Digite de forma completa')
começo = 2016
while '31':
    data = int(input('Digite o dia que começamos a namorar: '))
    if data == 31:
         print('Parabéns, você acertou !!!')
         sleep(3)
         aniver = atual - começo
         print(f'Temos exatamente {aniver} anos de namoro, MUITOOOOO TEMPO !!')
         break
        

    else:
        print('Você errou, Tente novamente.')
sleep(3)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
print('Tem algumas coisas que eu quero te dizer, porém, você precisa me ganhar Par ou Impar.')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
sleep(3)
while True:
    Aghata = int(input('Digite um valor: '))
    Renan = randint (0, 10)
    total = Aghata + Renan
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('\nPar ou Impar [P/I]: ')).strip().upper()[0]
    print(f'Aghata jogou {Aghata} e Renan jogou {Renan}. Total foi {total} ', end= ' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')   
    if tipo == 'P':
        if total % 2 == 0:
            print('Parabéns, você VENCEU !')
            print('\nAgora podemos continuar.')
            break
        else:
            print('Você PERDEU, tente novamente.')
    elif tipo == 'I':
        if total % 2 == 1:
            print('Parabéns, você VENCEU !')
            print('\nPodemos continuar.')
            break
        else:
            print('Você PERDEU, Tente novamente.')
            
print('Bom, tem várias coisas que eu quero te dizer.')
print('Porém, vou listar algumas.')
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
sleep(2)

print('Aqui vai as opções para você escolher.\n')
opção = 0
while opção != 6:
    
    print('=-' * 50)
    
    
    print('''          [1] Para abrir Primeira opção.
          [2] Para abrir Segunda opção.
          [3] Para abrir Terceira opção.
          [4] Para abrir Quarta opção.
          [5] Para abrir Quinta opção.
          [6] Para sair''')
    
    opção = int(input('Escolha e Digite a opção desejada: '))
    print('=-' * 50)
    
    if opção == 1:
        print('Você é e sempre será a pessoa mais especial para mim, a pessoa que sempre me apoia')
        sleep(1)
        print('E que está comigo em todos os momentos, sejam eles bons ou ruins.\n')
    elif opção == 2:
        print('Cada momento ao seu lado, é um presente para mim e cada segundo sem você só faz meu amor aumentar.\n')
    elif opção == 3:
        print('Eu amo o seu sorriso, seu jeito de cuidar de mim, de rir das minhas piadas e bobeiras sem graças que eu faço')
        sleep(1)
        print('O seu jeito de me olhar, de cuidar de mim é tudo perfeito.\n')
    
    elif opção == 4:
        print('Parece que até foi ontem quando começamos a conversar e você ficou me enrolando por 1 ano kkk')
        sleep(1)
        print('Mas, sei que valeu apena esperar, porque tudo aconteceu de uma forma tão perfeita.\n')
    elif opção == 5:
        print('Sei que não sou a melhor pessoa do mundo')
        sleep(1)
        print('A mais bonita ou a mais inteligente.')
        sleep(1)
        print('Mas posso te afirmar que, dia após dia, farei de tudo para te fazer a mulher mais feliz desse mundo.!\n')
    elif opção == 6:
        print('Obrigado por me aturar até aqui.')
        sleep(1)
        print('Sempre que quiser lembrar de mim, nem que seja um pouco')
        sleep(1)
        print('Estarei aqui.\n')
        print('Até mais.')
        sleep(6)
        break
    