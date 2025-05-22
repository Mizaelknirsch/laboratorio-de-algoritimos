import random
aleatorio =[random.randint(1, 50) for i in range(10)]
print(f"os numeros originais são {aleatorio}")
pares = [i for i in aleatorio if i % 2 == 0]
print("Números pares:", pares)
impares = [i for i in aleatorio if i % 2 != 0]
print("Números ímpares:", impares)
