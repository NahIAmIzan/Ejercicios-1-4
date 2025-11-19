iteraciones = 1_000_000  
pi_aprox = 0.0
for k in range(iteraciones):
    termino = (-1)**k / (2*k + 1)
    pi_aprox += termino

pi_aprox *= 4
print(f"Aproximación de π con {iteraciones} iteraciones:")
print(pi_aprox)