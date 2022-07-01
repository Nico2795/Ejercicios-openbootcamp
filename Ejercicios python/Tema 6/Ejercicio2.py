class Alumno :

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
   
        if self.nota >= 50 :
            print("Felicidades",self.nombre , "Has aprobado")

        else:
            print("Lastima", self.nombre , "mejor suerte para la proxima")

        

alumno1 =Alumno("Nico", 100)
alumno2=Alumno("Barbi", 40)
