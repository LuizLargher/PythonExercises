modo = int(input('Bem vindo à Calculadora\n Escolha o modo de operação baseado nos números abaixo:\n1) Adição\n2) Subtração\n3) Multiplicação\n4) Divisão\nQual operação você deseja fazer?'))
val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
rpadc = val1 + val2
rpsub = val1 - val2
rpmul = val1 * val2
rpdiv = int(val1 / val2)
if modo == 1:
    print('A soma dos valores é {}'.format(rpadc))
elif modo == 2:
    print('A subtração dos valores é {}'.format(rpsub))
elif modo == 3:
    print('A multiplicação dos valores é {}'.format(rpmul))
elif modo == 4:
    print('A divisão dos valores é {}'.format(rpdiv))
else:
    print('Escolha um número de 1 a 4')