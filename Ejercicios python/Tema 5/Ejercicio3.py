def añobisiesto (año = int(input("Introduce un año "))):

    if año % 4 == 0  and año % 100 != 0:
        print("Felicidades es un año bisiesto")
    
    else:
        print("No es un año bisiesto")

añobisiesto()
