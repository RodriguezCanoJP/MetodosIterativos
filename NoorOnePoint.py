
import time
from math import exp
import numpy as np

def noor_one_point(f, x0, tol, iterMax):
    """

    Función de Noor's One-Point para encontrar la raíz de una ecuación.
    
    Parámetros:
        f: Función a la que se le buscará la raíz.
        x0: Aproximación inicial.
        tol: Tolerancia para detener el método.
        iterMax: Número máximo de iteraciones permitidas.
    
    Resultados:
        x: Aproximación de la raíz encontrada.
        error: Valor absoluto de f(x), que se toma como el error en la aproximación.
        k: Número de iteraciones realizadas.
        tiempo: Tiempo de ejecución del método en segundos.
    """
    
    # Iniciar el temporizador para medir el tiempo de ejecución
    start_time = time.time()
    
    # Inicializar variables
    x = x0
    k = 0           # Contador de iteraciones
    error = float('inf')     # Error inicial (inicializado en infinito)
    
    # Iterar hasta alcanzar el número máximo de iteraciones
    while k < iterMax:
        # Calcular el valor de la función en la aproximación actual
        f_x = f(x)
        
        # Calcular la derivada numérica en la aproximación actual utilizando diferencias finitas
        f_prime_x = (f(x + tol) - f(x - tol)) / (2 * tol)

        # Manejar el caso donde la derivada es aproximadamente cero
        if abs(f_prime_x) < 1e-10:
            # Evitar la división por cero, ajustando ligeramente la derivada
            f_prime_x = 1e-10
        
        # Actualizar la aproximación utilizando el método de Noor's One-Point de segundo orden
        x = x - f_x / f_prime_x
        
        # Calcular el nuevo error absoluto (valor absoluto de f(x))
        error = abs(f_x)
        
        # Comprobar si se ha alcanzado la tolerancia deseada
        if error < tol:
            break  # Salir del bucle si se cumple la condición de parada
        
        # Incrementar el contador de iteraciones
        k += 1
    
    # Detener el temporizador y registrar el tiempo de ejecución
    tiempo = time.time() - start_time
    
    return x, error, k, tiempo

# Define tu función f(x)
def f(x):
    return exp(x)-x-10

# Llama a la función steffensen_secant
x0 = 1.5
tol = 1e-10
iterMax = 1000

start = time.time()
xk, err, k, tiempo_ejec = noor_one_point(f, x0, tol, iterMax)
stop = time.time()

print("Xk:", xk)
print("Error:", err)
print("Número de iteraciones:", k)
print("Tiempo de ejecución:", "{:.10f}".format(tiempo_ejec), "segundos")
print(f"Training time: {stop - start}s")


