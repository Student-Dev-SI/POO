
package exercicioaula5;

public class ContaBanco {
    public int numConta;
    protected String tipoConta;
    private String nomeTitular;
    private float saldoConta;
    private boolean statusConta;
    
    public ContaBanco(String cliente, String tipoConta){
        abrirConta(tipoConta, cliente);
        setSaldoConta(0);
        setStatusConta(false);
    }
        
    public void setNumConta(int numConta){
        this.numConta = numConta;
    }
    public int getNumConta(){
        return this.numConta;
    }
    
    public void setTipoConta(String tipoConta){
        this.tipoConta = tipoConta;
    }
    public String getTipoConta(){
        return this.tipoConta;
    }
    
    public void setNomeTitular (String nomeTitular){
        this.nomeTitular = nomeTitular;
    }
    public String getNomeTitular (){
        return this.nomeTitular;
    }
    
    public void setSaldoConta(float saldoConta){
        this.saldoConta = saldoConta;
    }
    public float getSaldoConta(){
        return this.saldoConta;
    }
    
    public void setStatusConta(boolean statusConta){
        this.statusConta = statusConta;
    }
    public boolean getStatusConta(){
        return this.statusConta;
    }
    
     
    public void abrirConta(String tipoConta, String nomeCliente){
        this.setStatusConta(true);
        this.setTipoConta(tipoConta);
        
        this.setNomeTitular(nomeCliente);
        //setNumConta(numConta);
        
        if (this.getTipoConta() == "CC"){
            this.setSaldoConta(50);
        }else if (tipoConta == "CP") {
            this.setSaldoConta(150);
        }
    }
    public void fecharConta(){
        if (this.getSaldoConta() == 0){
            //zerar dados;
            this.setStatusConta(false);
            System.out.println("Conta Fechada");
        }else if (this.getSaldoConta() > 0){
            System.out.println("ERRO! Você possui saldo na conta");
        }else if (this.getSaldoConta() < 0){
            System.out.println("ERRO! Você possui saldo devedor. Regularize sua conta");
        }
    }
    public void depositar(float valorDeposito){
        if (this.getStatusConta()){
            this.setSaldoConta(this.getSaldoConta() + valorDeposito);
            System.out.println ("Seu saldo agora: " + this.getSaldoConta());
        }else {
            System.out.println("Conta inativa");
        }        
    }
    
    public void sacar(float valorSaque){
        if(this.getStatusConta() == true){
            if(valorSaque <= this.getSaldoConta()){// verificar se consigo sacar mesmo com valor negativo 
                this.setSaldoConta(this.getSaldoConta() - valorSaque );
                
                System.out.println("Saque realizado. /n Seu Saldo agora: " + this.getSaldoConta());
            }else{
                System.out.println("Você não tem saldo suficiente para realizar esta operação. \n Seu saldo: "+ this.getSaldoConta());
            }
        }else{
            System.out.println("Conta inativa");
        }
    }
    public void pagarmensal(){
        float valorM = 0;
        if (getTipoConta() == "CC"){
            valorM = 12.00f;
        }else if (getTipoConta() == "CP"){
            valorM = 20.00f;
        }        
        setSaldoConta(getSaldoConta() - valorM);
        
        System.out.println("Mensalidade paga no valor de "+ valorM +"/n seu saldo agora é de "+ getSaldoConta());
    }
    
    public void status(){
        System.out.println("Numero da Conta: " +getNumConta());
        System.out.println("Tipo conta: " +getTipoConta());
        System.out.println("Titular: " +getNomeTitular());
        System.out.println("Saldo: " +getSaldoConta());
        System.out.println("Ativo: " +getStatusConta());        
    }
}
