frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(junto,'  ', inverso)
if junto == inverso:
    print('Está frase é um PALÍNDROMO.')
else:
    print('Está frase não é um PALÍNDROMO')
    