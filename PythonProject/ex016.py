numeros = []
num = int(input("Quantos números deseja inserir? "))

for i in range(num):
    valor = int(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            # troca
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Lista ordenada:", numeros)