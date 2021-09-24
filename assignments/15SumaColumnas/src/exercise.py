def generaMatriz (renglon, columna):
    # Completar esta función
    pass


def sumaColumnas (matriz):
    # Completar esta función
    pass


def main():
    renglon = int(input())
    columna = int(input())
    if renglon>=1 and columna>=1:
        matriz = generaMatriz (renglon, columna)
        vectorSuma = sumaColumnas(matriz)
        print (vectorSuma)
    else:
        print("Error")


if __name__=='__main__':
    main()
