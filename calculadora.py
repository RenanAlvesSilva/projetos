opção = 0
while opção != 5:
    print('================= Calculadora ==============')
    n1 = int(input('Entre com primeiro valor: '))
    n2 = int(input('Entre com o segundo valor: '))
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] DIVIDIR
    [5] SAIR''')
    
    
    opção = int(input('Qual sua opção: '))
    print('=x=x=x=x=x=x=x=x=x=x=x=x==x=x=')
    if opção == 1:
      soma = n1 + n2
      print(f'{n1} + {n2} = {soma}')
      print('-----------------------------')
    elif opção == 2:
        mult = n1 * n2
        print(f'{n1} x {n2} = {mult}')
        print('----------------------------')
    elif opção == 3:
        if n1 > n2:
         print(f'O maior número foi {n1}') 
         print('----------------------------')
        if n1 < n2:
            print(f'O maior número foi {n2}')
            print('--------------------------')
    elif opção == 4:
        div = n1 / n2
        print(f'{n1} % {n2} = {div:.2f}')
        print('-----------------------------')
    elif opção == 5:
        print('Programa Fechado')
        print('Obrigado por utilizar.')
    else:
        print('*** A T E N Ç Ã O ***')
        print('Opção INVÁLIDA.')
        print('Por Favor, entre com uma opção VÁLIDA.')
