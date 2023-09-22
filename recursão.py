import time

# CONTAGEM REGRESSIVA

def contagem_regressiva(número):
    for i in range(número, 0, -1):
       print(i)
       time.sleep(1)
 
print("10 segundos para decolagem!:")
contagem_regressiva(10)

# SOMA RECURSIVA

def soma_recursiva(i: int):
    if( i <= 1): return 1
    else:
        return i + soma_recursiva(i-1)
    
print ("Aqui está as somas recusivas!")
print(f"de 1: {soma_recursiva(1)}") 
print(f"de 2: {soma_recursiva(2)}") 
print(f"de 3: {soma_recursiva(3)}") 
print(f"de 4: {soma_recursiva(4)}") 
print(f"de 5: {soma_recursiva(5)}") 

# STRINGS INVERTIDAS

def inverter_string(s):
    if len(s) == 0: return ""
    else: return s[-1] + inverter_string(s[:-1])

print("Aqui está as strings invertidas!")
print(f'boca : {inverter_string("boca")}')
print(f'cabo : {inverter_string("cabo")}')
print(f'marrocos : {inverter_string("marrocos")}')
print(f'constituição : {inverter_string("constituição")}')