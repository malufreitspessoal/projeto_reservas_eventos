from datetime import datetime
from utilitarios.funcoes import colunas

 # lista de dicionarios
#mais pra frente criar um bd real

class Cliente:
    def __init__(self, nome, cpf, email, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.data_nascimento = data_nascimento
        
        
    @classmethod
    def criar_user(cls):
        while True:
            cpf = input('Insira seu CPF (somente números): ').strip()
           
            if not cpf.isdigit(): 
                print('CPF inválido. Digite apenas números.') 
                continue  
            
            if any(cliente['cpf'] == cpf for cliente in cls.bd):
                print('Já existe um usuário com esse CPF!')
                return
            break

        nome = input('Informe seu nome completo: ').upper().strip()  
        
        data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ') 
        
        email = input('Informe seu melhor email: ').upper().strip()      
        novo_usuario =cls(nome, cpf, email , data_nascimento) 
        
        print('Usuário cadastrado com sucesso')
        # print(Cliente.bd)  
        return novo_usuario
     
    @staticmethod  # que ai ele não precisa receber self
    def fazer_login(cpf):
        cliente = next((cliente for cliente in Cliente.bd if cliente['cpf'] == cpf), None)
        if cliente:
            
            return cliente  # Retorna o cliente encontrado
        else:
            return False


    def editar_user(self):
        pass
    
    def realizar_compra():
        pass
        

