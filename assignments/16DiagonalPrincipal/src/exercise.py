def diagonal_principal (matriz):
    # Completar esta función
    pass


def leer (ren, col):
    # Completar esta función
    pass


def main():
    ren = int(input())
    col = int(input())
    if (ren != col):
        print ("La matriz no es cuadrada")
    else:
        matriz = leer (ren, col)
        vector_diagonal = diagonal_principal(matriz)
        print (vector_diagonal)


if __name__=='__main__':
    main()
