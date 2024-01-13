package aula07;

import java.util.Random;

public class Luta {
    private Lutador desafiado;
    private Lutador desafiante;
    private int rounds;
    private boolean aprovada;

    public Lutador getDesafiado() {
        return this.desafiado;
    }

    public void setDesafiado(Lutador desafiado) {
        this.desafiado = desafiado;
    }

    public Lutador getDesafiante() {
        return this.desafiante;
    }

    public void setDesafiante(Lutador desafiante) {
        this.desafiante = desafiante;
    }

    public int getRounds() {
        return rounds;
    }

    public void setRounds(int rounds) {
        this.rounds = rounds;
    }

    public boolean getAprovada() {
        return aprovada;
    }

    public void setAprovada(boolean aprovada) {
        this.aprovada = aprovada;
    }
    
    
    public void marcarLuta(Lutador ldesafiante ,Lutador ldesafiado){
        if (ldesafiante.getCategoria() == ldesafiado.getCategoria() && ldesafiante != ldesafiado){
            this.setAprovada(true);
            this.setDesafiado(ldesafiado);
            this.setDesafiante(ldesafiante);
        }else {
            this.setAprovada(false);
            this.setDesafiado(null);
            this.setDesafiante(null);
            System.out.println("Não posso marcar luta");
        }
    }
    public void lutar(){
         if (this.getAprovada()){
            System.out.println("________________ DESAFIADO ________________");
            desafiado.apresentar();
            System.out.println("________________ DESAFIANTE _______________");
            desafiante.apresentar();
            
            Random aleatorio = new Random();
            int vencedor = aleatorio.nextInt(3);    //0 1 2
                          
            switch(vencedor){
                case 0:
                    System.out.println("\n Empate\n");
                    desafiante.empatarLuta();
                    desafiado.empatarLuta();
                    break;
                case 1:
                    System.out.println("\n\n Vitória do: "+this.desafiado.getNome()+"\n\n");
                    desafiado.ganharLuta();
                    desafiante.perderLuta();                  
                    break;
                case 2:
                    System.out.println("\n\n Vitória do: "+this.desafiante.getNome()+"\n\n");
                    desafiante.ganharLuta();
                    desafiado.perderLuta();
                    break;
             }
         }else{
             System.out.println("Luta não pode acontecer");
         }
    }
}
