# from Reserva import Reserva
from utilitarios.funcoes import colunas
from Models.Cliente import Cliente
from Models.Organizador import Organizador
from Models.Evento import Evento
from Controllers.requisicoes import *
'''
Se criamos várias funcoes de menu, o objeto que a gente criar nao vai ser possivel ser chamado ou complica mais por exemplo quero chamar o objeto organizador
'''
def obter_opcao_menu(opcoes):
    """
    Solicita ao usuário uma opção de menu e garante que a entrada seja válida.

    Args:
        opcoes (list): Uma lista de strings representando as opções de menu válidas.

    Returns:
        str: A opção de menu escolhida pelo usuário (em maiúsculas e sem espaços extras).
    """
    while True:
        opcao = input('').upper().strip()
        if opcao in opcoes:
            return opcao
        else:
            print('Opção inválida, tente novamente')


def menu():
    """
    Exibe o menu de login principal, permitindo que o usuário faça login, cadastre-se ou acesse o menu de organizador.
    """
    while True:
        print(f'''
            {colunas()} Bem vindo ao Eventlu - O melhor dos eventos se encontra aqui! {colunas()}

            LO - Fazer login
            CA - Cadastrar novo usuário

            ADMIN - Para Organizadores
            SAIR - Sair
        ''')

        opcao = obter_opcao_menu(['LO', 'CA', 'ADMIN', 'SAIR'])
        
        match opcao:
            case 'LO':
                print(f" {colunas()} Oie ! Eventlu já estavá com saudade {colunas()}")
                cpf = input('Insira seu CPF (somente números): ').strip()
                if Cliente.fazer_login(cpf) != False:
                    while True:
                        print(f'''
                            {colunas()} Bem vindo de volta {obj_cliente.nome} {colunas()}

                            RC - Realizar compra
                            EC - Exibir compra
                            CC - Cancelar compra

                            SAIR - Sair
                        ''')

                        opcao = obter_opcao_menu(['RC', 'EX', 'CC', 'SAIR'])
                        match opcao:
                            case 'RC':
                                pass
                            case 'SAIR':
                                break
                else:
                    print("CPF não encontrado. Faça o cadastro.")

            case 'CA':
                obj_cliente = Cliente.criar_user()
                cadastrar_cliente()

            
            case 'ADMIN':
                while True:
                    print(f'''
                        {colunas()} Bem vindo Organizador {colunas()}

                        LO - Fazer login
                        CA - Cadastrar nova empresa

                        SAIR - Sair
                    ''')

                    opcao = obter_opcao_menu(['LO', 'CA', 'SAIR'])
                    match opcao:
                        case 'LO':
                            print(f" {colunas()} Fala Organizador ! Eventlu já estavá com saudade {colunas()}")
                            cnpj = input('Insira CNPJ (somente números): ').strip()
                            organizador_instancia = Organizador.fazer_login(cnpj)
                            
                            if organizador_instancia:
                                
                                while True:
                                    print(f'''
                                        Bem vindo ao Eventlu {organizador_instancia.nome} 

                                        CA - Cadastrar novo Evento
                                        EB - Exibir seus eventos
                                        EX - Excluir evento cadastrado

                                        SAIR - Sair
                                    ''')

                                    opcao = obter_opcao_menu(['CA', 'EB', 'EX', 'SAIR'])
                                    match opcao:
                                        case 'CA':
                                            Evento.criar_evento(organizador_instancia.nome)

                                        case 'EB':
                                            pass

                                        case 'Ex':
                                            pass

                                        case 'SAIR':
                                            print('Valeu, falou')
                                            break

                                        case '_':
                                            print('Opcão inválida')
                                    

                        case 'CA':
                            obj_organizador = Organizador.criar_organizador()

                        case 'SAIR':
                            print('Quero te ver em breve hein? Até mais')
                            break

                        case '_':
                            print('Opção Inválida, tente novamente')

