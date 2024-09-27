import numpy as np

# Aqui se define uma função para calcular fatorial

matA = np.zeros([3,4])
matB= np.zeros([3,4])

for i in range(0, matA.shape[0]):
    for j in range(0, matA.shape[1]):
        matA[i][j] = int(input(f"Digite o Elemento da {i+1}ª linha; {j+1}ª coluna: "))

        matB[i][j]1
         = matA[i][j] * 3
        

print(f"MATRIZ A: \n{matA}")
print(f"MATRIZ B: \n{matB}")
