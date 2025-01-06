import itertools
import math
import random
import matplotlib.pyplot as plt

# Definindo as coordenadas das cidades
cities = {
    'Sao Paulo': (-23.5505, -46.6333),
    'Rio de Janeiro': (-22.9068, -43.1729),
    'Brasilia': (-15.8267, -47.9218),
    'Salvador': (-12.9714, -38.5014),
    'Porto Alegre': (-30.0346, -51.2177),
    'Curitiba': (-25.4284, -49.2733),
    'Fortaleza': (-3.7172, -38.5433),
    'Recife': (-8.0476, -34.8770),
}

diesel_cost_per_liter = 5.82  
vehicle_consumption_km_per_liter = 8  

def haversine_distance(city1, city2):
    lat1, lon1 = map(math.radians, cities[city1]) 
    lat2, lon2 = map(math.radians, cities[city2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    R = 6371.0  
    return R * c  

def total_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += haversine_distance(route[i], route[i + 1])
    distance += haversine_distance(route[-1], route[0])  
    return distance

def calculate_fuel_cost(total_distance, diesel_cost_per_liter, vehicle_consumption_km_per_liter):
    cost_per_km = diesel_cost_per_liter / vehicle_consumption_km_per_liter
    total_cost = total_distance * cost_per_km
    return total_cost

def find_shortest_route_brute_force(cities):
    city_names = list(cities.keys())
    all_routes = itertools.permutations(city_names)
    shortest_route = None
    shortest_distance = float('inf')

    for route in all_routes:
        if route[0] != 'Sao Paulo':  
            continue
        distance = total_distance(route)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_route = route

    return shortest_route, shortest_distance

def calcular_distancia(rotas):
    distancia = 0
    for i in range(len(rotas)):
        p1 = rotas[i]
        p2 = rotas[(i + 1) % len(rotas)]
        distancia += haversine_distance(p1, p2)
    return distancia

def inicializa_populacao(tamanho_populacao, city_names):
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = city_names.copy()
        random.shuffle(individuo)
        populacao.append(individuo)
    return populacao

def selecao(populacao):
    tournament_size = min(5, len(populacao))  # Ajustar o tamanho do torneio
    nova_populacao = []
    while len(nova_populacao) < len(populacao) // 2:
        torneio = random.sample(populacao, tournament_size)
        vencedor = min(torneio, key=lambda x: calcular_distancia(x))
        nova_populacao.append(vencedor)
    return nova_populacao

def cruzamento(pai1, pai2):
    tamanho = len(pai1)
    ponto1, ponto2 = sorted(random.sample(range(tamanho), 2))

    filho = [None] * tamanho
    filho[ponto1:ponto2] = pai1[ponto1:ponto2]

    pointer = 0
    for gene in pai2:
        if gene not in filho:
            while filho[pointer] is not None:
                pointer += 1
            filho[pointer] = gene
    
    return filho

def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            j = random.randint(0, len(individuo) - 1)
            individuo[i], individuo[j] = individuo[j], individuo[i]

def algoritmo_genetico(cities, tamanho_populacao=300, taxa_mutacao=0.15, geracoes=1000):
    city_names = list(cities.keys())
    populacao = inicializa_populacao(tamanho_populacao, city_names)

    for _ in range(geracoes):
        if len(populacao) < 2:
            print("População muito pequena para continuar.")
            break

        populacao = selecao(populacao)
        nova_populacao = populacao.copy()

        while len(nova_populacao) < tamanho_populacao:
            if len(populacao) < 2:
                print("População muito pequena para cruzamento.")
                break
            pai1, pai2 = random.sample(populacao, 2)
            filho = cruzamento(pai1, pai2)
            mutacao(filho, taxa_mutacao)
            nova_populacao.append(filho)

        mix_size = min(len(populacao), tamanho_populacao // 10)
        if mix_size > 0:
            nova_populacao += random.sample(populacao, mix_size)

        nova_populacao = list(set(tuple(ind) for ind in nova_populacao))[:tamanho_populacao]

    melhor_individuo = min(nova_populacao, key=lambda x: calcular_distancia(x))
    return melhor_individuo, calcular_distancia(melhor_individuo)

def simulate_travel_time(route, speed_kmh):
    total_time = 0
    times = []

    for i in range(len(route) - 1):
        distance = haversine_distance(route[i], route[i + 1])
        time_hours = distance / speed_kmh  
        total_time += time_hours
        times.append(total_time)

    distance = haversine_distance(route[-1], route[0])
    time_hours = distance / speed_kmh
    total_time += time_hours
    times.append(total_time)

    return times

# Definir a velocidade média (em km/h)
speed_kmh = 60  

# Calculando as rotas
brute_force_route, brute_force_dist = find_shortest_route_brute_force(cities)
ga_route, ga_dist = algoritmo_genetico(cities)

# Simulando o tempo de viagem
brute_force_times = simulate_travel_time(brute_force_route, speed_kmh)
ga_times = simulate_travel_time(ga_route, speed_kmh)

# Calculando o custo da viagem
brute_force_cost = calculate_fuel_cost(brute_force_dist, diesel_cost_per_liter, vehicle_consumption_km_per_liter)
ga_cost = calculate_fuel_cost(ga_dist, diesel_cost_per_liter, vehicle_consumption_km_per_liter)

# Exibindo os resultados
print("Força Bruta - Rota mais curta:")
print(" -> ".join(brute_force_route), f"\nDistância total: {brute_force_dist:.2f} km")
print(f"Tempo total de viagem a {speed_kmh} km/h: {brute_force_times[-1]:.2f} horas")
print(f"Custo total de viagem: R$ {brute_force_cost:.2f}\n")

print("Algoritmo Genético - Rota mais curta:")
print(" -> ".join(ga_route), f"\nDistância total: {ga_dist:.2f} km")
print(f"Tempo total de viagem a {speed_kmh} km/h: {ga_times[-1]:.2f} horas")
print(f"Custo total de viagem: R$ {ga_cost:.2f}\n")

# Plotando os gráficos
labels = ['Força Bruta', 'Algoritmo Genético']
distances = [brute_force_dist, ga_dist]
costs = [brute_force_cost, ga_cost]

# Criando um gráfico com linhas
plt.figure(figsize=(10, 6))

# Gráfico da Distância
plt.subplot(2, 1, 1)
plt.plot(labels, distances, marker='o', linestyle='-', color='blue', label='Distância (km)')
plt.title('Comparação de Distâncias e Custos')
plt.ylabel('Distância (km)')
plt.ylim(0, max(distances) * 1.1)
plt.grid(True)
for i, v in enumerate(distances):
    plt.text(i, v + 1, f"{v:.2f}", ha='center')

# Gráfico do Custo
plt.subplot(2, 1, 2)
plt.plot(labels, costs, marker='o', linestyle='-', color='red', label='Custo (R$)')
plt.ylabel('Custo (R$)')
plt.ylim(0, max(costs) * 1.1)
plt.grid(True)
for i, v in enumerate(costs):
    plt.text(i, v + 1, f"{v:.2f}", ha='center')

plt.tight_layout()
plt.show()