def converTempCels_Fahr(temp):
    Fahr = temp * 1.8 + 32
    return Fahr

def converTempFahr_Cels(temp):
    cels = (temp - 32) * 5/9
    return cels

while True:
    print("\n1 - Celsius para Fahrenheit ")
    print("2 - Fahrenheit para Celsius ")
    print("3 - Sair")
    opcao = int(input("Escolha a Opção a qual você quer converter: "))

    if opcao == 1:
        temp = float(input("Digite a temperatura: "))
        print(f"A temperatura {temp} em Celsius vale {converTempCels_Fahr(temp):.2f} em Fahrenheit")
    elif opcao == 2:
        temp = float(input("Digite a temperatura: "))
        print(f"A temperatura {temp} em Fahrenheit vale {converTempFahr_Cels(temp):.2f} em Celsius ")
    elif opcao == 3:
        print("Saindo...")
        break
    else:
        print("ERRO! escolha uma das opções!")