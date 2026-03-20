def sequecFibon(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        n1, n2 = 0, 1
        for _ in range (2, num+1):
            n1, n2 = n2, n1 + n2
        return n2
num = int(input("Digite um número: "))
print(f"Esse numero corresponde ao numero {sequecFibon(num)} na sequência de Fibonacci")