import random

def calcular_pi_monte_carlo(num_pontos):
    
    pontos_dentro_do_circulo = 0

    for _ in range(num_pontos):
        # Gera coordenadas aleatórias entre -1 e 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Calcula a distância do ponto até a origem
        distancia = x**2 + y**2

        # Se a distância for menor ou igual a 1, o ponto está dentro do círculo
        if distancia <= 1:
            pontos_dentro_do_circulo += 1

    # Estima PI
    pi_estimado = 4 * (pontos_dentro_do_circulo / num_pontos)
    return pi_estimado

# Exemplo 
num_pontos = 1000000  # Quanto maior o número de pontos, mais precisa será a estimativa
pi_estimado = calcular_pi_monte_carlo(num_pontos)

print(f"Estimativa de PI com {num_pontos} pontos: {pi_estimado}")
print(f"Valor real de PI (para comparação): {3.141592653589793}")