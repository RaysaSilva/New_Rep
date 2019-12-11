from string import ascii_letters
print("olá")
print('New branch')

frase = 'Ola, eu sou uma frase. Me quebre em palavras e conte quantas palavras eu contenho'
lista_de_palavras = frase.split(' ')
nova_palavra = ''
lista = []
for palavras in lista_de_palavras:
    for letras in palavras:
        if letras in ascii_letters:
            nova_palavra = nova_palavra + letras
    if nova_palavra not in lista:
        lista.append(nova_palavra)
        nova_palavra = ''
        
print(lista)
print(len(lista))
                