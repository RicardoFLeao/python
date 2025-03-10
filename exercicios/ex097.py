def escreva(frase):
    tam = len(frase) + 4
    print('~' * tam)
    print(f'{frase}'.center(tam))
    print('~' * tam)


escreva('Estou ficando fera de mais')
escreva('ricardo'.capitalize())
escreva('Amanda')