
package aula04;


public class Aula04 {

    public static void main(String[] args) {
        Caneta c1 = new Caneta("B","red",0.8f);// posso iniciar ja setando os parametros do meu metodo construtor
        //c1.setModelo("BIC"); 
        //c1.modelo = "bic"; ##consigo alterar manualmente pois a variavel é publica##

        //c1.setPonta(0.5f);
        //c1.ponta = 0.5f; ##nao consigo alterar pq é privado
       
        //System.out.println("Tenho uma Caneta "+ c1.getModelo()+ " com ponta "+c1.getPonta());
        //c1.status();
        
        Caneta c2 = new Caneta("BIC","Azul",0.5f);
        //c2.status();
    }
    
}
