import numpy as np

# Importando o numpy

try:
    #vetor nos quais vão ser adicionados os numeros
    vet1 = np.zeros(10)
    vet2 = np.zeros(10)

    #vetor que vai conter a Subtração dos numeros
    vetSub = np.zeros(10)

    for i in range(0,len(vet1)):
        vet1[i] = float(input(f"Digite o {i+1}º elementos do Primeiro Vetor:"))
        vet2[i] = float(input(f"Digite o {i+1}º elementos do Segundo Vetor:"))

        # vai buscar com base no indici o valores correspondentes, somar os dois e adicionar ao 3º
        vetSub[i] = vet1[i] - vet2[i]

    print(f"Os valores do vetor um são: {vet1}")
    print(f"Os valores do vetor dois são: {vet2}")
    print(f"O valor da soma dos vetore um e dois são: {vetSub}")

except:
    print("Por favor digite um número!")