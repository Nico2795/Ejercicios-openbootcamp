from datetime import datetime



t = datetime.now()

horaactual = t.time()


fechaproximasalida = datetime(2022,7,5,19,0,0,0)
fechasalidahoy= datetime(2022,7,4,19,0,0,0)

falta = fechaproximasalida - t

if t > fechasalidahoy :
    print("Ya puedes irte a casa, son las", horaactual)

if t < fechaproximasalida:
    print("Aun faltan " , falta, "para poder volver a salir")


    
