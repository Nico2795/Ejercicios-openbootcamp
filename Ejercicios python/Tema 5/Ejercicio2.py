def numerosPrimos (numero=int(input("Introduce un numero"))):

    if numero > 1:
        for n in range(2,numero):
            if numero % n  == 0:
                print("Lastima, no es un numero primo")
                break
        
            elif numero % n != 0:
                print("Felicidades, encontraste un numero primo")
                break

    else:
        print("Error! recuerda que debes elegir un numero mayor a 1 y que sea un entero")

numerosPrimos()
    
