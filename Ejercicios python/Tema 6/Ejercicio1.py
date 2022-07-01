
class Vehiculo :
    def __init__(self,Color, Ruedas, Puertas):
        self.Color = Color
        self.Ruedas = Ruedas
        self.Puertas = Puertas
        print(Color, Ruedas, Puertas)

class Coche(Vehiculo):
    def __init__(self, Color, Ruedas, Puertas,Velocidad,Cilindrada):
        super().__init__(Color, Ruedas, Puertas)
        self.Velocidad=Velocidad
        self.Cilindrada = Cilindrada

        print(Color, Ruedas, Puertas,Velocidad,Cilindrada)

c=Vehiculo("rojo",4,4)

