import numpy as np

try:
    # definir vet a ser populado
    vet = np.zeros(10)

    # vet q vai conter x²
    vetQuad = np.zeros(10)

    for i in range(0,len(vet)):
        vet[i] =  float(input(f"Digite o {i+1}º valor do vetor: "))
        #vai calcular o x²
        vetQuad[i] = (vet[i]**2)

    print(f"Os números são: \n{vet}")
    print(f"Seus respectivos valores ao quadrado são: \n{vetQuad}")


except: 
    print("Digite um número!")
