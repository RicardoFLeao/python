v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
mai = v1
men = v1
if v2 > mai:
    mai = v2
if v3 > mai:
    mai = v3
if v2 < men:
    men = v2
if v3 < men:
    men = v3
print('O menor valor é: {}'.format(men))
print('O maior valor é: {}'.format(mai))
