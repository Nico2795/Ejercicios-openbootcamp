class Alumno :

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
         print("Nombre:", self.nombre)
         print("Nota:", self.nota)
    def notas (self):
        if self.nota >= 50 :
            print("Felicidades",self.nombre , "Has aprobado")

        else:
            print("Lastima", self.nombre , "mejor suerte para la proxima")

        

alumno1 =Alumno("Nico", 100)
alumno2=Alumno("Barbi", 40)

alumno1.imprimir()
alumno1.notas()
alumno2.imprimir()
alumno2.notas()

