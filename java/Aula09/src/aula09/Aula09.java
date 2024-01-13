package aula09;
public class Aula09 {
    public static void main(String[] args) {
        Pessoa leitor = new Pessoa("Pedro",25,'M');
         
        System.out.println("Nome: "+leitor.getNome());
        System.out.println("Sexo:"+leitor.getSexo());
        System.out.println("Idade: "+leitor.getIdade()+" anos");        
        
        Livro cronicas = new Livro("Cronicas de um inventor", "Clarice Lispector",200, leitor);
        
        cronicas.abrir();
        cronicas.folhear(50);
        
        cronicas.avancarPag();
        
        cronicas.detalhes();
        
        System.out.println(cronicas.toString());
    }
}
