vocabulario = ('aprender', 'programar', 'estudar', 'linguagem', 'phyton', 'curso', 'gratis', 'estudar', 'praticar', 'computador', 'trabalhar', 'futuro')
for palavra in vocabulario:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for vogais in palavra:
        if vogais.upper() in 'AEIOU':
            print(vogais.upper(), end=' ')