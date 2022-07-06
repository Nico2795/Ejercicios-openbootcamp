import pickle

class Vehiculo:
    velocidad = 0.0
    color = ""

    def __init__(self, velocidad, color,):
        self.velocidad = velocidad
        self.color = color

    def __str__(self):
        return f"Mi auto tiene un color {self.color} , y va a una velocidad de {self.velocidad} km/h "

    def getvelocidad (self):
        return self.velocidad


v = Vehiculo(120, "Rojo")


f = open("datos.bin", "wb")
pickle.dump(v,f)
f.close()

f = open("datos.bin" , "rb")
leerdatos = pickle.load(f)
f.close()


print(leerdatos)
print(leerdatos.getvelocidad())
