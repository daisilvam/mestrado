# i. Números Primos até N
def numeros_primos_ate_n(n):
# Encontra todos os números primos até n usando o Crivo de Eratóstenes.

    if n < 2:
        return []

    # Cria uma lista booleana 'e_primo' e inicializa todos os elementos como True.
    # A lista tem tamanho n+1 para incluir o número n.
    e_primo = [True] * (n + 1)
    e_primo[0] = e_primo[1] = False  # 0 e 1 não são primos

    # Percorre a lista a partir do 2.
    for i in range(2, int(n**0.5) + 1):
        # Se i ainda for primo
        if e_primo[i]:
            #marca todos os seus múltiplos como não-primos.
            for multiplo in range(i * i, n + 1, i):
                e_primo[multiplo] = False

    # Cria uma lista com os números que são primos.
    primos = [i for i, eh_primo in enumerate(e_primo) if eh_primo]

    return primos

#Exemplo
N = 30
primos_encontrados = numeros_primos_ate_n(N)
print(f"Números primos até {N}: {primos_encontrados}")