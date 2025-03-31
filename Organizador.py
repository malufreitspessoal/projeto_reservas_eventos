from Evento import Evento
from datetime import datetime, date

bd = []
eventos = []

class Organizador:
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
            
            if any(cliente['cnpj'] == cnpj for cliente in bd):
                print('Já existe uma empresa com esse CNPJ!')
                return
            break

        nome = input('Informe o nome da empresa: ')  
        
        email = input('Informe email: ')       
        
        novo_organizador =cls(nome, cnpj, email) 
        bd.append({'nome': novo_organizador.nome,
                    'cnpj' : novo_organizador.cnpj,
                    'email': novo_organizador.email
                    }) 
        
        print('Empresa cadastrada com sucesso')  
        return novo_organizador
    
    def criar_evento(self):
        nome_evento = input('Nome do evento: ').strip().upper()
        descricao_evento = input('Descrição do evento: ').strip().upper()
        faixa_etaria = input('Faixa etária do evento: ').strip().upper()
        
        while True:
            try:
                data_evento = input('Data do evento: ').strip()
                data_objeto = datetime.strptime(data_evento, "%d/%m/%Y")
                data_reformada = data_objeto.date()
                data_atual = date.today()
                
                if data_atual > data_reformada:
                    print('Data não pode ser maior que o dia atual')
                
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.") 
            novo_evento = Evento(nome_evento, descricao_evento, self.nome, faixa_etaria, data_objeto)
            
            eventos.append({
                'nome_evento': novo_evento.nome_evento,
                'descricao_evento': novo_evento.descricao_do_evento,
                'organizador': self.nome,
                'faixa_etaria': novo_evento.faixa_etaria,
                'data_evento': data_objeto.strftime("%d/%m/%Y")
                            })
            print('Evento criado com sucesso')
            return novo_evento
        
    @staticmethod
    def fazer_login(cnpj):
        cliente = next((cliente for cliente in bd if cliente['cnpj'] == cnpj), None)
        if cliente:
            print(f"Bem-vindo(a), {cliente['nome']}!")
            return cliente  
        else:
            print("CNPJ não encontrado. Faça o cadastro.")
            return None
    
    
    def exibir_eventos():
        pass
    
    
    def excluir_evento():
        pass
    
    
    
  
                       
  