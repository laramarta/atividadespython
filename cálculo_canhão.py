# Alunas: Lara Marta e Nicole Evelin
# Tentamos mas não sabemos as fórmulas de matemática :(

import math

def c_velocidade_inicial (força, angulo):
    v_i = math.sqrt (2 * força / 0.5) * math.sin(math.radians(a))
    return v_i

def c_tempo_de_voo (v_i, angulo, força):
    t_v = (2 * v_i * math.sin(math.radians(a))) / 12
    return t_v

def c_local_da_queda (v_i, angulo, x, y):
    t_v = c_tempo_de_voo
    q_x = c_x + (v_i * math.cos(math.radians(a)) * t_v )
    q_y = c_y + (v_i * math.sin(math.radians(a)) * t_v ) - (0.5 * 10 * t_v ** 2)
    return q_x, q_y

def c_velocidade (v_i, angulo, tempo):
    v_v = v_i * math.sin(math.radians(angulo)) - 10 * tempo_voo
    v_h = v_i * math.cos(math.radians(angulo))
    return v_v, v_h

def c_distancia (q_x):
    q_x = c_local_da_queda
    d_h = q_x - 8
    return d_h

velocidade_inicial = c_velocidade_inicial 
tempo_voo = c_tempo_de_voo 
q_y = c_local_da_queda
distancia_horizontal = c_distancia
v_v = c_velocidade

print (f"Vamos calcular!")

c_y = float(input("Digite o valor da coordenada y do canhão: "))
c_x = float(input("Digite o valor da coordenada x do canhão: "))
c_f = float(input("Digite o valor da força em newtons: "))
a = float(input("Digite o valor do ângulo em graus: "))


print (f"1°) A velociadade inicial do lançamento é: {velocidade_inicial} m/s")
print (f"2°) O tempo total do voo do projetil é: {tempo_voo} s")
print (f"3°) O local de queda do projetil é: x = y {q_y} m")
print (f"4°) As velocidades verticais e horizontais do projetil em cada instante de voo é: {v_v}")
print (f"5°) A distância horizontal entre o ponto de lançamento e o local da queda é: {distancia_horizontal} m")