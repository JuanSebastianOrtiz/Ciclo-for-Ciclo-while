 #ejercicios de ejemplos de bucles
#programador :Juan sebastian ortiz ibarra 
#vérsion 1.0 
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")