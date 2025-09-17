# ii. Fatorial de N
def fatorial_recursivo(n):
    # Calcula o fatorial de um número inteiro não negativo n usando recursão.
    if n < 0:
        return "Erro: O fatorial não é definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

# uso 1
numero = 5
resultado = fatorial_recursivo(numero)
print(f"O fatorial de {numero} é {resultado}")

#Uso 2
numero = 0
resultado = fatorial_recursivo(numero)
print(f"O fatorial de {numero} é {resultado}")