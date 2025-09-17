# c. Busca em lista ordenada
def busca_binaria(lista, elemento):
   #Realiza uma busca binária em uma lista ordenada.
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if lista[meio] == elemento:
            return meio  # elemento encontrado!
        elif lista[meio] < elemento:
            inicio = meio + 1  # Busca na metade direita da lista
        else:
            fim = meio - 1  # Busca na metade esquerda da lista
    
    return None  # O elemento não foi encontrado

# Exemplo
lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
elemento_procurado = 23

indice_encontrado = busca_binaria(lista_ordenada, elemento_procurado)

if indice_encontrado is not None:
    print(f"O elemento {elemento_procurado} foi encontrado no índice {indice_encontrado}.")
else:
    print(f"O elemento {elemento_procurado} não foi encontrado na lista.")