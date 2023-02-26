# Definição da string a ser invertida
string = "exemplo"

# Conversão da string para uma lista de caracteres
lista_de_caracteres = list(string)

# Cálculo do índice do meio da lista
meio = len(lista_de_caracteres) // 2

# Inversão dos caracteres utilizando um loop
for i in range(meio):
    j = len(lista_de_caracteres) - 1 - i
    lista_de_caracteres[i], lista_de_caracteres[j] = lista_de_caracteres[j], lista_de_caracteres[i]

# Conversão da lista de caracteres de volta para uma string
string_invertida = "".join(lista_de_caracteres)

# Impressão da string invertida
print(string_invertida)
