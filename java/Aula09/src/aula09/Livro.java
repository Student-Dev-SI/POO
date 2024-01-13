package aula09;
public class Livro implements Publicacao {
    private String titulo;
    private String autor;
    private int totPaginas;
    private int pagAtual;
    private boolean aberto;
    private Pessoa leitor;

    public Livro(String titulo,String autor, int totPaginas, Pessoa leitor){
        this.setTitulo(titulo);
        this.setAutor(autor);
        this.setTotPaginas(totPaginas);
        this.setLeitor(leitor);
        this.setAberto(false);
    }
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getTotPaginas() {
        return totPaginas;
    }

    public void setTotPaginas(int totPaginas) {
        this.totPaginas = totPaginas;
    }

    public int getPagAtual() {
        return pagAtual;
    }

    public void setPagAtual(int pagAtual) {
        this.pagAtual = pagAtual;
    }

    public boolean isAberto() {
        return aberto;
    }

    public void setAberto(boolean aberto) {
        this.aberto = aberto;
    }

    public Pessoa getLeitor() {
        return leitor;
    }

    public void setLeitor(Pessoa leitor) {
        this.leitor = leitor;
    }
    
    public void detalhes(){
        System.out.println("_______INFORMAÇÕES_______");
        System.out.println("Titulo: "+this.getTitulo());
        System.out.println("Autor: "+this.getAutor());
        System.out.println("Total de paginas: "+this.getTotPaginas());
        System.out.println("Página atual: "+this.getPagAtual());
        System.out.println("esta aberto? "+this.isAberto());
        System.out.println("Leitor: "+this.leitor.getNome());
        System.out.println("_________________________");
    }

    @Override
    public void abrir() {
        if (!this.isAberto()){
            this.setAberto(true);
            this.setPagAtual(1);
        }else{
            System.out.println("Ja esta aberto");
        }
    }

    @Override
    public void fechar() {
        if (this.isAberto()){
            this.setPagAtual(0);
            this.setAberto(false);
        }else{
            System.out.println("Ja esta fechado");
        }
    }

    public void folhear(int pag) {
        if (this.getTotPaginas() > pag){
            this.setAberto(true);
            this.setPagAtual(pag);
        }else {
            System.out.println("Pagina não existe");
        }
    }

    @Override
    public void avancarPag() {
        if (this.isAberto()){
            if (this.getPagAtual()< this.getTotPaginas()){
                this.setPagAtual(this.getPagAtual()+1);
            }else{
                System.out.println("Você terminou a leitura");
            }
            
        }
    }

    @Override
    public void voltarPag() {
        if (this.isAberto()){
            if (this.getPagAtual()>1){
                this.setPagAtual(this.getPagAtual()-1);
            }
        }
    }

    @Override
    public String toString() {
        return "Livro{" + "titulo=" + titulo + ", autor=" + autor + ", totPaginas=" + totPaginas + ", pagAtual=" + pagAtual + ", aberto=" + aberto + ", leitor=" + leitor + '}';
    }
    
}
