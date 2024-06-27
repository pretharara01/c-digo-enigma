mapa = {
'6': 'F',
'5': 'E',
'50': 'L',
'1': 'I',
'26': 'Z',
'MM': 2000,
'R': 18,
}



mensagem = "6550126MMR"

letras = ''
numeros = ''

i = 0


while i < len(mensagem):
    chave = mensagem[i:i + 2]
    if chave in mapa:
        i = i + 2
    else:
        chave = mensagem[i]
        i += 1


    if chave in mapa:
        valor = mapa[chave]
        if isinstance(valor, int):
            numeros += str(valor)
        else:
            letras += valor

print(letras, numeros[0:2] + numeros[4:6])
