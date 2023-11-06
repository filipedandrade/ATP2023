#TPC8: Teste de aferição
#Resolva os problemas apresentados a seguir.
# tpc-1. Especifique as seguintes listas em compreensão:
# a) Lista formada pelos elementos que não são comuns às duas listas:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
comuns = [item for item in lista1 if item in lista2]
lista1_sem_comuns = [item for item in lista1 if item not in comuns]
lista2_sem_comuns = [item for item in lista2 if item not in comuns]
resultado = lista1_sem_comuns + lista2_sem_comuns

print(resultado)
# Resultado esperado: [1,2,3,5,7,8]

# b) Lista formada pelas palavras do texto compostas por mais de 3 letras:
texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""

palavras = []
palavra = ''
for caracter in texto:
    if caracter == ' ' or caracter == '\n':
        if palavra:  
            palavras.append(palavra)
            palavra = ''
    else:
        palavra += caracter
if palavra:  
    palavras.append(palavra)


lista = []
for palavra in palavras:
    contador = 0
    for letra in palavra:
        contador += 1
    if contador > 3:
        lista.append(palavra)

print(lista)
# Resultado esperado: ['Vivia', 'poucos', 'anos', 'algures', 'concelho', ...]

# c) Lista formada por pares do tipo (índice, valor) com os valores da lista dada:
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = []
i = 1
for valor in lista:
    listaRes.append((i, valor))
    i += 1
print(listaRes)
# Resultado esperado: [(1,'anaconda'), (2,'burro'), (3,'cavalo'), (4,'macaco')]