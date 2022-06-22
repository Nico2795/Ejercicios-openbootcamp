public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente ();
        cliente.nombre = "Me llamo Nico";
        cliente.edad = 15;
        cliente.telefono = 3312;
        cliente.credito = "santander";
        
        System.out.println(cliente.edad);
        System.out.println(cliente.nombre);
        System.out.println(cliente.telefono);
        System.out.println(cliente.credito);
        
        


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

