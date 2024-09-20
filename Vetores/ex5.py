import numpy as np

try:
    tam = int(input(f"Digite o tamnho do vetor: "))

    # Vai criar vets com base no tamanho digitado
    vetA = np.zeros(tam)
    vetB = np.zeros(tam)

    for i in range(0, len(vetA)):
        vetA[i] = float(input(f"Digite o {i+1}º número do vetor: "))

        # Verifica se o indice é par, se for o valor que ocupa o indice é x
        # *3, se não x/2
        if ((i%2)==0): 
            vetB[i] = (vetA[i] * 3)        
        else:
            vetB[i] = (vetA[i] / 2)


    print(f"Os valores do vetor um são: {vetA}")
    print(f"Os valores do vetor dois são: {vetB}")

except:
    print("Por favor digite um número!")