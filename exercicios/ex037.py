num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] Conversão para BINARIO
[ 2 ] Conversão para OCTAL
[ 3 ] Conversão para HEXADECIMAL ''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} convertido para BINARIO é: {}'.format(num, bin(num)[2:]))
elif opcao ==2:
    print('O número {} convertido para OCTAL é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXDECIMAL é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! tente novamente.')
