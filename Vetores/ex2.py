import numpy as np

# Aqui se define uma função para calcular fatorial
def fat(num):
    fat = 1
    for i in range(1, num + 1):
        fat *= i
    return fat

# vet com os 10 elementos
vet = np.arange(1,11)

# vet q vai conter o n! 
w = np.zeros(10, dtype=int)

for i in range(0,len(vet)):
    # usando a func pré-declarada para calcular fat!
    w[i] = fat(vet[i])

# mostra os numeros de 1 a 10 dps seus fat!
print(f"Os números são: \n{vet}")
print(f"Seus respectivos fatoriais são: \n{w}")

