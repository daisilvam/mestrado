def multiplicar_matrizes(matriz1, matriz2):

    linhas_m1 = len(matriz1)
    colunas_m1 = len(matriz1[0])
    linhas_m2 = len(matriz2)
    colunas_m2 = len(matriz2[0])

  
    if colunas_m1 != linhas_m2:
        print("Erro: O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.")
        return None


    matriz_resultado = [[0 for _ in range(colunas_m2)] for _ in range(linhas_m1)]

  
    for i in range(linhas_m1):
        for j in range(colunas_m2):
            for k in range(colunas_m1):
                matriz_resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return matriz_resultado


matriz_a = [[1, 2, 3], [4, 5, 6]]
matriz_b = [[7, 8], [9, 10], [11, 12]]

resultado = multiplicar_matrizes(matriz_a, matriz_b)

if resultado:
    print("Matriz A:")
    for linha in matriz_a:
        print(linha)

    print("\nMatriz B:")
    for linha in matriz_b:
        print(linha)
    
    print("\nResultado da multiplicação:")
    for linha in resultado:

        print(linha)
