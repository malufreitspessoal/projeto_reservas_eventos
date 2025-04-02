
class Organizador:
    bd = []
    def __init__(self, nome, cnpj, email):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
    
    @classmethod
    def criar_organizador(cls):
        while True:
            cnpj = input('Insira CNPJ (somente números): ').strip()
           
            if not cnpj.isdigit(): 
                print('CNPJ inválido. Digite apenas números.') 
                continue  
            
            if any(cliente['cnpj'] == cnpj for cliente in Organizador.bd):
                print('Já existe uma empresa com esse CNPJ!')
                return
            break

        nome = input('Informe o nome da empresa: ')  
        
        email = input('Informe email: ')       
        
        novo_organizador =cls(nome, cnpj, email) 
        Organizador.bd.append({'nome': novo_organizador.nome,
                    'cnpj' : novo_organizador.cnpj,
                    'email': novo_organizador.email
                    }) 
        
        print('Empresa cadastrada com sucesso')  
        return novo_organizador
        
    @staticmethod
    def fazer_login(cnpj):
        for organizador_info in Organizador.bd:  # Itera sobre a lista bd
            if organizador_info['cnpj'] == cnpj:
                print(f"Bem-vindo(a), {organizador_info['nome']}!")
                # Cria uma instância de Organizador com os dados encontrados
                organizador_instancia = Organizador(organizador_info['nome'], organizador_info['cnpj'], organizador_info['email'])
                return organizador_instancia  # Retorna a instância
        
        print("CNPJ não encontrado. Faça o cadastro.")
        return None
    
    
    def exibir_eventos():
        pass
    
    
    def excluir_evento():
        pass
    
    
    
  
                       
  