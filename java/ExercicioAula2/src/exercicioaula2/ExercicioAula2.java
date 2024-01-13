
package exercicioaula2;


public class ExercicioAula2 {

    public static void main(String[] args) {
        Calendario cn = new Calendario();
        
        cn.ano = 2019;
        cn.mes = "Maio";
        cn.dia = 8;
        cn.temEvento = false;
        cn.dataEspecial = false;
        cn.fds = false;
        
        cn.criarEvento(9, "Maio", 2019);
        cn.informarData();
    }
    
}
