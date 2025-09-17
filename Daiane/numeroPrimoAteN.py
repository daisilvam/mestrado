def numeros_primos_ate_n(n):

    if n < 2:
        return []

    e_primo = [True] * (n + 1)
    e_primo[0] = e_primo[1] = False  

   
    for i in range(2, int(n**0.5) + 1):
       
        if e_primo[i]:
         
            for multiplo in range(i * i, n + 1, i):
                e_primo[multiplo] = False

  
    primos = [i for i, eh_primo in enumerate(e_primo) if eh_primo]

    return primos


N = 30
primos_encontrados = numeros_primos_ate_n(N)

print(f"Números primos até {N}: {primos_encontrados}")
