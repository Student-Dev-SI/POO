package exercicioaula2;

public class Calendario {
    //atributos
    int dia;
    String mes;  
    int ano;
    boolean dataEspecial;
    boolean temEvento;
    String evento;
    int diaEvento;
    String mesEvento;
    int anoEvento;
    boolean fds;

    void criarEvento(int d, String m, int a ){
        if (d != 0 && m != "" && a != 0){
            this.diaEvento = d;
            this.mesEvento = m;
            this.anoEvento = a;
            this.temEvento = true;
        }
        System.out.println("Evento criado para "+ this.diaEvento +" de "+ this.mesEvento + " de " + this.anoEvento);
    }
    
    void informarData(){
        System.out.println("Hoje é dia "+this.dia+" de "+this.mes+" de "+this.ano);
        System.out.println("Hoje é fim de semana? "+this.fds);
        System.out.println("É uma data especial? "+this.dataEspecial);
        System.out.println("tem evento?"+this.temEvento);
        System.out.println("Evento para o dia "+ this.diaEvento +" de "+ this.mesEvento + " de " + this.anoEvento);
    }
}
