
num1 = float(input('Digite um número para dividir: '))
num2 = float(input('Digite por quanto você quer dividir: '))
while num2 == 0:
    print("ERRO! Não é possível dividir por ZERO!")
    num2 = float(input('Digite outro valor por qual você quer dividir: '))

print(f"O valor da divisão de {num1} por {num2} é {num1/num2:.2f}")