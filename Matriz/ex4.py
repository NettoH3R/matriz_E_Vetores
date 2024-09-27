import numpy as np

# Aqui se define uma função para calcular fatorial

matA = np.zeros([3,3])
matB= np.zeros([3,3])
matC= np.zeros([3,3])

for i in range(0, matA.shape[0]):
    for j in range(0, matA.shape[1]):
        matA[i][j] = int(input(f"Digite o Elemento da {i+1}ª linha; {j+1}ª coluna da matriz A: "))

print("\n")

for i in range(0, matA.shape[0]):
    for j in range(0, matA.shape[1]):
        matB[i][j] = int(input(f"Digite o Elemento da {i+1}ª linha; {j+1}ª coluna da matriz B: "))


for i in range(0, matA.shape[0]):
    for j in range(0, matA.shape[1]):
        matC[i][j] = matA[i][j] + matB[i][j]
        
print("\n")
print(f"MATRIZ A: \n{matA}")
print(f"MATRIZ B: \n{matB}")
print(f"MATRIZ C: \n{matC}")
