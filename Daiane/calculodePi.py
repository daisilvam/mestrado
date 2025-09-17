import random

def calcular_pi_monte_carlo(num_pontos):
    
    pontos_dentro_do_circulo = 0

    for _ in range(num_pontos):
     
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        
        distancia = x**2 + y**2

        
        if distancia <= 1:
            pontos_dentro_do_circulo += 1


    pi_estimado = 4 * (pontos_dentro_do_circulo / num_pontos)
    return pi_estimado


num_pontos = 1000000 
pi_estimado = calcular_pi_monte_carlo(num_pontos)

print(f"Estimativa de PI com {num_pontos} pontos: {pi_estimado}")

print(f"Valor real de PI (para comparação): {3.141592653589793}")
