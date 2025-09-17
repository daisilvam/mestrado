# b. Ordenação de listas (mais de 1000 inteiros)
import random

# Cria uma lista de 1000 inteiros aleatórios
lista_inteiros = [random.randint(0, 10000) for _ in range(1000)]

# Ordena a lista de forma crescente e cria uma nova lista ordenada
lista_ordenada = sorted(lista_inteiros)

# Imprime a primeira parte da lista ordenada para ver o resultado
print("Lista original (primeiros 10 elementos):")
print(lista_inteiros[:10])
print("\nLista ordenada (primeiros 10 elementos):")
print(lista_ordenada[:10])