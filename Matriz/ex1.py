import numpy as np

# Aqui se define uma função para calcular fatorial

mat = np.zeros([5,5])
dig = []
da = []
db = []

for i in range(0, mat.shape[0]):
    for j in range(0, mat.shape[1]):
        mat[i][j] = int(input(f"Digite o Elemento da {i+1}ª linha; {j+1}ª coluna: "))


        if i < j:
            num = mat[i][j]
            da.append(num)

        if i == j:
            num = mat[i][j]
            dig.append(num)
        
        if i < j:
            num = mat[i][j]
            db.append(num)

print(f"Diagonal principal:{da}")
print(f"Acima da Diagonal principal:{da}")
print(f"Abaixo da Diagonal principal:{db}")