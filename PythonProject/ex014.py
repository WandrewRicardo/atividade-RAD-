import string
def verif_Poli(text):
    text = text.lower()
    text = text.replace(" ", "")
    text = text.translate(str.maketrans('', '', string.punctuation))
    invertido = text[::-1]
    if(text == invertido):
        print('Isso é um Políndromo')
    else:
        print("Isso não é um Políndromo")

text = str(input("Digite uma frase: "))
verif_Poli(text)

