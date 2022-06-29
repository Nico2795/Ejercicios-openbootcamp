numero_inicio = int (input("Introduce un numero "))
numero_final = int (input ("Introduce otro numero "))
numero_impar = [int]

for numero_impar in range (numero_inicio , numero_final +1):
    if numero_impar % 2 !=0:
        print(f"Esta es la lista de numero impares entre {numero_inicio} y {numero_final}")
        print (numero_impar)

        
