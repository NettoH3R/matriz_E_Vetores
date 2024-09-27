import numpy as np

def exibir_elementos_matriz_secundaria(matriz):
    diagonal_secundaria = np.fliplr(matriz).diagonal()  # Diagonal secundária
    acima_diagonal_secundaria = matriz[np.triu_indices(5, k=1)[::-1]]  # Acima da diagonal secundária
    abaixo_diagonal_secundaria = matriz[np.tril_indices(5, k=-1)[::-1]]  # Abaixo da diagonal secundária

    # Exibindo os resultados
    print("\nElementos da diagonal secundária:", diagonal_secundaria)
    print("Elementos acima da diagonal secundária:", acima_diagonal_secundaria)
    print("Elementos abaixo da diagonal secundária:", abaixo_diagonal_secundaria)


print("Digite os elementos da matriz 5x5 (25 elementos separados por espaço):")
elementos = list(map(int, input().split()))


matriz = np.array(elementos).reshape(5, 5)


print("\nMatriz 5x5:")
print(matriz)

exibir_elementos_matriz_secundaria(matriz)