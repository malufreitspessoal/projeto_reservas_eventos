from utilitarios.funcoes import colunas
from classes.Cliente import Cliente
from classes.Organizador import Organizador

class Menu:
    def exibir_mensagem_saida(mensagem):
        print(mensagem)

    def obter_opcao_menu(opcoes):
        while True:
            opcao = input('').upper().strip()
            if opcao in opcoes:
                return opcao
            else:
                print('Opção inválida, tente novamente.')

    def menu_cliente():
        while True:
            print(f'''
                {colunas} Bem vindo Cliente {colunas}

                LO - Fazer login
                CA - Cadastrar novo usuário

                SAIR - Sair
            ''')

            opcao = Menu.obter_opcao_menu(['LO', 'CA', 'SAIR'])

            match opcao:
                case 'LO':
                    print(f" {colunas} Oie ! Eventlu já estava com saudade {colunas}")
                    cpf = input('Insira seu CPF (somente números): ').strip()
                    cliente = Cliente.fazer_login(cpf)
                    if cliente:
                        # Aqui você pode adicionar o menu específico para clientes logados
                        print("Login realizado com sucesso!")
                    else:
                        print('CPF não encontrado ou incorreto. Tente novamente.')
                case 'CA':
                    Cliente.criar_user()
                case 'SAIR':
                    Menu.exibir_mensagem_saida('Quero te ver em breve hein? Até mais')
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
                    print(f" {colunas} Oie ! Eventlu já estava com saudade {colunas}")
                    cpf = input('Insira seu CPF (somente números): ').strip()
                    cliente = Cliente.fazer_login(cpf)
                    if cliente:
                        Menu.menu_cliente()
                    else:
                        print('CPF não encontrado ou incorreto. Tente novamente.')
                case 'CA':
                    Cliente.criar_user()
                case 'ADMIN':
                    Menu.menu_admin()
                case 'SAIR':
                    Menu.exibir_mensagem_saida('Quero te ver em breve hein? Até mais')
                    break

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
                    print(f" {colunas} Fala Organizador ! Eventlu já estava com saudade {colunas}")
                    cnpj = input('Insira CNPJ (somente números): ').strip()
                    organizador = Organizador.fazer_login(cnpj)
                    if organizador:
                        Menu.menu_login_admin()
                    else:
                        print('CNPJ não encontrado ou incorreto. Tente novamente.')
                case 'CA':
                    Organizador.criar_organizador()
                case 'SAIR':
                    Menu.exibir_mensagem_saida('Quero te ver em breve hein? Até mais')
                    break

    def menu_login_admin():
        while True:
            print(f'''
                Bem vindo ao Eventlu - {Organizador.nome}

                CA - Cadastrar novo Evento
                EB - Exibir seus eventos
                EX - Excluir evento cadastrado

                SAIR - Sair
            ''')

            opcao = Menu.obter_opcao_menu(['CA', 'EB', 'EX', 'SAIR'])

            match opcao:
                case 'CA':
                    Organizador.criar_evento()
                case 'EB':
                    # Implementar exibição de eventos
                    pass
                case 'EX':
                    # Implementar exclusão de eventos
                    pass
                case 'SAIR':
                    Menu.exibir_mensagem_saida('Valeu, falou')
                    break

# Exemplo de uso:
Menu.menu_login()