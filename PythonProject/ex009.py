with open ("texto.docx", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
conteudo = conteudo.strip()
palavras = conteudo.split()
print(f'o numero de palavras dentro do arquivo é: {len(palavras)}')
