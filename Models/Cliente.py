from datetime import datetime
from utilitarios.funcoes import colunas

 # lista de dicionarios
#mais pra frente criar um bd real

class Cliente:
    bd = []
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

        nome = input('Informe seu nome completo: ')  
        
        data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ') 
        
        email = input('Informe seu melhor email: ')       
        novo_usuario =cls(nome, cpf, email , data_nascimento) 
        Cliente.bd.append({'nome': novo_usuario.nome,
                    'cpf' : novo_usuario.cpf,
                    'data_nascimento': novo_usuario.data_nascimento,
                    'email': novo_usuario.email
                    }) 
        
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
        

