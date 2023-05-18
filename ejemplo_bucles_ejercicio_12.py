 #ejercicios de ejemplos de bucles
#programador :Juan sebastian ortiz ibarra 
#vérsion 1.0 
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))