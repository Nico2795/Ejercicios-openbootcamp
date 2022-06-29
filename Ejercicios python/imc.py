peso = (input("Introduce tu peso en kg "))
estatura = (input("introduce tu estatura en metros "))

imc = round(float(peso)/ float(estatura)**2,2)
print("tu indice de masa corporal es " + str(imc))
