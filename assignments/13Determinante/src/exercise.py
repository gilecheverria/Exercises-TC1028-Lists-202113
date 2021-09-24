def determinante(matriz):
    # Completar esta función
    pass

def leer_matriz_por_renglon():
    # Completar esta función
    pass

def main():
    matriz = leer_matriz_por_renglon()
    if (len(matriz) != 2 or len(matriz[0])!= 2):
        print("La matriz no es una matriz de 2x2")
    else:
        resultado = determinante(matriz)
        print(resultado)


if __name__=='__main__':
    main()
