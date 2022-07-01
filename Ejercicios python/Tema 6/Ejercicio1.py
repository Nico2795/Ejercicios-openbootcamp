class Vehiculo:
    Color = "Rojo"
    Ruedas = 4
    Puertas = 4

class Coche(Vehiculo):
    Velocidad = "120 km/h"
    Cilindrada= "50 cc"

c = Coche()
print(c.Velocidad)
