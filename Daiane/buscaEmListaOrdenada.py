
def busca_binaria(lista, elemento):
   
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if lista[meio] == elemento:
            return meio 
        elif lista[meio] < elemento:
            inicio = meio + 1  
        else:
            fim = meio - 1 
    
    return None  


lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
elemento_procurado = 23

indice_encontrado = busca_binaria(lista_ordenada, elemento_procurado)

if indice_encontrado is not None:
    print(f"O elemento {elemento_procurado} foi encontrado no índice {indice_encontrado}.")
else:

    print(f"O elemento {elemento_procurado} não foi encontrado na lista.")
