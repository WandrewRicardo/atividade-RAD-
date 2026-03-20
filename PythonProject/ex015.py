import re
text = input("Digite uma frase: ")
palavras = re.findall(r'\b\w+\b', text)

cont_palavras = len(palavras)
print("Número de palavras:", cont_palavras)