pimport java.util.*;

public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente ();
        Trabajador trabajador = new Trabajador();
        cliente.nombre = "Nico";
        cliente.edad = 15;
        cliente.telefono = 3312;
        cliente.credito = "santander";
        
      System.out.println("Soy " + cliente.nombre + ", tengo " + cliente.edad + " años , " + "mi numero de telefono es  " + cliente.telefono + ", y mi credito es del " + cliente.credito);
      
        trabajador.nombre = "Barbi";
        trabajador.edad = 26;
        trabajador.telefono= 7618;
        trabajador.salario = 5000000;
        
        System.out.println("Soy " + trabajador.nombre + ", tengo" + trabajador.edad + " años, " + "mi numero de telefono es " + trabajador.telefono + ", y mi sueldo es " + trabajador.salario);
        
        


}
}


class Persona {
    int edad;
    String nombre;
    int telefono;
}

class Cliente extends Persona {
    String credito;
}
class Trabajador extends Persona {
    int salario;
}

