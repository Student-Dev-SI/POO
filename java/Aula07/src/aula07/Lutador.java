package aula07;

public class Lutador implements Controlador {
    private String nome;
    private String nacionalidade;
    private int idade;
    private float altura;
    private float peso;
    private String categoria;
    private int vitorias;
    private int derrotas;
    private int empates;

    public Lutador(String nome, String nacionalidade, int idade, float altura, float peso, int vitorias, int derrotas, int empates) {
        this.setNome(nome);
        this.SetNacionalidade(nacionalidade);
        this.setIdade(idade);
        this.setAltura(altura);
        this.setPeso(peso);
        this.setVitorias(vitorias);
        this.setDerrotas(derrotas);
        this.setEmpates(empates);
    }
    
    public String getNome(){
        return this.nome;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public String getNacionalidade(){
        return this.nacionalidade;
    }
    public void SetNacionalidade(String nacionalidade){
        this.nacionalidade = nacionalidade;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public float getAltura() {
        return altura;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }

    public float getPeso() {
        return peso;
    }

    public void setPeso(float peso) {
        this.peso = peso;
        setCategoria(peso);
    }

    public String getCategoria() {
        return categoria;
    }

    private void setCategoria(float peso) {
        String cat = "";
        
        if (peso <= 52.2){
            cat ="Peso Inválido";
        }else if (peso <= 70.3){
            cat ="Peso Leve";
        }else if (peso <= 83.9){
            cat = "Peso Médio";
        }else if (peso <= 120.2){
            cat = "Peso Pesado";
        }else{
            cat = "Peso Inválido";
        }
        
        this.categoria = cat;
    }

    public int getVitorias() {
        return vitorias;
    }

    public void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }

    public int getDerrotas() {
        return derrotas;
    }

    public void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }

    public int getEmpates() {
        return empates;
    }

    public void setEmpates(int empates) {
        this.empates = empates;
    }

    @Override
    public void apresentar() {
        System.out.println("=======APRESENTACAO========");
        System.out.println("Lutador : "+ this.getNome());
        System.out.println("com "+this.getIdade()+ " de idade");
        System.out.println("Nacionalidade: "+ this.getNacionalidade());
        System.out.println("com: "+this.getPeso()+ " de peso");
        System.out.println("e "+this.getAltura()+ " de altura");
        System.out.println("categoria: "+ getCategoria());
        System.out.println("com "+this.getVitorias() +"vitórias, "+this.getEmpates()+ "empates, "+this.getDerrotas()+"derrotas");
        System.out.println("===========================");        
    }

    @Override
    public void status() {
        System.out.println("Nome : "+this.getNome());
        System.out.println("categoria: "+getCategoria());
        System.out.println("vitórias: "+this.getVitorias());
        System.out.println("empates: "+this.getEmpates());
        System.out.println("derrotas: "+this.getDerrotas());
    }

    @Override
    public void ganharLuta() {
        setVitorias(this.getVitorias()+1);
    }

    @Override
    public void perderLuta() {
        setDerrotas(this.getDerrotas()+1);
    }

    @Override
    public void empatarLuta() {
        setEmpates(this.getEmpates()+1);
    }
    
}