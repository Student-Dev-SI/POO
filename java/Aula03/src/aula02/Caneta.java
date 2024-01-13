/* foi ensinado sobre controle de acesso a metodos, atributos na classe e nos objetos*/

package aula02;

public class Caneta {
    public String modelo;
    public String cor;
    private float ponta;
    protected int carga;
    private boolean tampada;
    
    public void status(){
        System.out.println("modelo: "+ this.modelo);
        System.out.println("Uma caneta "+ this.cor);
        System.out.println("Ponta "+ this.ponta);
        System.out.println("carga "+ this.carga);
        System.out.println("Esta tampada "+ this.tampada);
            }
    public void rabiscar(){
        if (this.tampada == true){
            System.out.println("ERRO! não posso rabiscar");
        }else {
            System.out.println("Estou rabiscando");
        }
    }  
    protected void tampar (){
        this.tampada = true;
    }
    protected void destampar() {
        this.tampada = false;
    }
}
