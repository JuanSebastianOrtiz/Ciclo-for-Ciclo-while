 #ejercicios de ejemplos de bucles
#programador :Juan sebastian ortiz ibarra 
#vérsion 1.0 
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
 