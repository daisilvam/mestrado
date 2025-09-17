
def fatorial_recursivo(n):
  
    if n < 0:
        return "Erro: O fatorial não é definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)


numero = 5
resultado = fatorial_recursivo(numero)
print(f"O fatorial de {numero} é {resultado}")

numero = 0
resultado = fatorial_recursivo(numero)

print(f"O fatorial de {numero} é {resultado}")
