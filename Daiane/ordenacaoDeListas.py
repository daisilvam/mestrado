import random

lista_inteiros = [random.randint(0, 10000) for _ in range(1000)]

lista_ordenada = sorted(lista_inteiros)

print("Lista original (primeiros 10 elementos):")
print(lista_inteiros[:10])
print("\nLista ordenada (primeiros 10 elementos):")

print(lista_ordenada[:10])
