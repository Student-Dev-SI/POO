package aula02;

public class Aula02 {
    public static void main(String[] args) {
       Caneta c1 = new Caneta();  //instancia     
       c1.cor = "Azul"; //atribuindo valor
       c1.ponta = 0.5f;
       //c1.tampada = false;
       c1.tampar();
       //c1.destampar();
       c1.rabiscar();
       //c1.status();
       
       Caneta c2 = new Caneta();
       c2.cor = "Vermelha";
       c2.modelo = "Yasmin";
       c2.destampar();
       c2.rabiscar();
    }
    
}
