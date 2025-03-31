# from Reserva import Reserva
from utilitarios.funcoes import colunas
from classes.Cliente import Cliente, bd
from classes.Organizador import Organizador, bd
   
class Menu:
    
    def obter_opcao_menu(opcoes):
        while True:
            opcao = input('').upper().strip()
            if opcao in opcoes:
                return opcao
            else:
                print('Opção inválida, tente novamente')
    
    def menu_cliente():    
        while True:
            print(f'''
            {colunas} Bem vindo de volta {colunas}
            
            RC - Realizar compra
            EC - Exibir compra
            CC -  Cancelar compra
            
            SAIR - Sair
            
            ''')
        
            opcao = Menu.obter_opcao_menu(['RC', 'EX', 'CC', 'SAIR'])
            match opcao:
                case 'RC':
                    pass
                case 'SAIR':
                    break

    def menu_login():
        while True:
            print('''
            Bem vindo ao Eventlu - O melhor dos eventos se encontra aqui!          
            
            LO - Fazer login
            CA - Cadastrar novo usuário
            
            ADMIN - Para Organizadores
            SAIR - Sair
            
            ''')
        
            opcao = Menu.obter_opcao_menu(['LO', 'CA', 'ADMIN', 'SAIR'])
            match opcao:
                case 'LO':
                    print(f" {colunas} Oie ! Eventlu já estavá com saudade {colunas}")
                    cpf = input('Insira seu CPF (somente números): ').strip()
                    Cliente.fazer_login(cpf)
                    Menu.menu_cliente() 
                
                case 'CA':
                    Cliente.criar_user() 
                
                case 'ADMIN':
                    Menu.menu_admin()
                
                case 'SAIR':
                    print('Quero te ver em breve hein? Até mais')
                    break
                
                case '_':
                    print('Opção Inválida, tente novamente')
            
    def menu_admin():
        while True:
            print(f'''
            {colunas} Bem vindo Organizador {colunas}
            
            LO - Fazer login
            CA - Cadastrar nova empresa
            
            SAIR - Sair
            
            ''')
        
            opcao = Menu.obter_opcao_menu(['LO', 'CA', 'SAIR'])
            match opcao:
                case 'LO':
                    print(f" {colunas} Fala Organizador ! Eventlu já estavá com saudade {colunas}")
                    cnpj = input('Insira CNPJ (somente números): ').strip()
                    
                    organizador_instancia = Organizador.fazer_login(cnpj)
                    if organizador_instancia:
                        Menu.menu_login_admin(organizador_instancia) 
                             
                case 'CA':
                     Organizador.criar_organizador()
                    # return organizar_objeto
                case 'SAIR':
                    print('Quero te ver em breve hein? Até mais')
                    break
                
                case '_':
                       print('Opção Inválida, tente novamente')
             

                    
    def menu_login_admin(organizador_instancia):
        while True:
            print(f'''
                Bem vindo ao Eventlu - 
                
            
                CA - Cadastrar novo Evento
                EB - Exibir seus eventos
                EX - Excluir evento cadastrado
                
               
                SAIR - Sair
                
                ''')
            
            opcao = Menu.obter_opcao_menu(['CA', 'EB', 'EX', 'SAIR'])
            match opcao:
                case 'CA':
                    organizador_instancia.criar_evento()
                
                case 'EB':
                    pass
                                
                case 'Ex':
                    pass
                
                case 'SAIR':
                    print('Valeu, falou')
                    break
                
                case '_':
                    print('Opcão inválida')
