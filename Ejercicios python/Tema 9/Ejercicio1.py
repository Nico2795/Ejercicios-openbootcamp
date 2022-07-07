paisescoma = input("Introduce paises separados por coma \n")
paises = [pais for pais in paisescoma.split(",")]

print(list(sorted(set(paises))))
