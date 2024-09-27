import numpy as np

try:
    mat = np.zeros([5,5], dtype = int)
    matCol = np.zeros([5,1], dtype = int)

    for i in range(0, mat.shape[0]):
        for j in range(0, mat.shape[1]):
            mat[i][j] = int(input(f"Digite o Elemento da {i+1}ª linha; {j+1}ª coluna: "))

    coluna = int(input("Digite a coluna que deseja ver 1, 2, 3, 4 ou 5: "))

    if 1 <= coluna <=5 :
        for i in range(0, mat.shape[0]):
            matCol[i][0] = mat[i][coluna - 1]

        print(f"Matriz: \n{mat}")
        print(f"Coluna desejada: \n{matCol}")
    else:
        print("coluna não encontrada")

except:
    print("Valor inválido")