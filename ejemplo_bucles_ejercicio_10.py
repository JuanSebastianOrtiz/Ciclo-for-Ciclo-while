 #ejercicios de ejemplos de bucles
#programador :Juan sebastian ortiz ibarra 
#vérsion 1.0 
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")