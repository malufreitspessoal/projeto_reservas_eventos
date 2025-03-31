class Reserva:
    def __init__(self, quantidade_de_lugares:int):
        """ 
        Aqui eu indico o numero de pessoas que podem ter no evento
        crio uma lista de acordo com o número. Criei então outra lista para adicionar 
        futuramente os lugares que forem sendo reservados
        
        """
        self.quantidade_de_lugares = []
        self.lugares_reservados = []
        for i in range(1, quantidade_de_lugares +1):
            self.quantidade_de_lugares.append(i)
        

    def reservar_lugar(self, lugar_reservado:int)-> str:
        
        """
        Aqui o metodo é reservar o lugar, então ele confere se o lugar que ele quer reservar 
        está disponivel na lista "quantidade_de_lugares". Se estiver ele faz a remoção nessa lista e adiciona a lista criada
        "lugares_reservados"

        """
        self.lugar_reservado = lugar_reservado

        if self.quantidade_de_lugares == []:
             return f'Não há lugares disponíveis'
        
        if lugar_reservado in self.quantidade_de_lugares:
            
            self.quantidade_de_lugares.remove(lugar_reservado)
            self.lugares_reservados.append(lugar_reservado)
            self.lugares_reservados.sort()
            
            return f'Lugar {lugar_reservado} reservado com sucesso'  

        elif lugar_reservado in self.lugares_reservados:
            
            return f'Lugar {lugar_reservado} já está reservado'  
        
        
        
        else: 
             
             return f'Lugar inexistente'

    def cancelar_reserva(self, lugar_cancelado)-> str:
           
        """
        Aqui o metodo é cancelar o lugar já reservado, então ele confere se o lugar que ele quer reservar 
        está disponivel na lista "quantidade_de_lugares". Se estiver ele faz a remoção nessa lista e adiciona a lista criada
        "lugares_reservados"

        """
        self.lugar_cancelado = lugar_cancelado

        if lugar_cancelado in self.lugares_reservados:
            
            self.lugares_reservados.remove(lugar_cancelado)
            self.quantidade_de_lugares.append(lugar_cancelado)
            self.quantidade_de_lugares.sort()

            return f'Lugar {lugar_cancelado} cancelado com sucesso'
        
        elif lugar_cancelado in self.quantidade_de_lugares:
             
             return f'Esse lugar não foi reservado'


    def show_places_disponiveis(self)-> str:
            if self.quantidade_de_lugares == []:
                 return 'Não há mais lugares disponíveis'    
            
            return f'Os lugares disponíveis são {self.quantidade_de_lugares}'


# while True:
     
#      opcao = mostrar_menu()

#      match opcao:
        
#         case 1:
#             lugar_para_reservar = int(input('Qual lugar você gostaria de reservar? '))
#             print(aniversario.reservar_lugar(lugar_para_reservar))
        
#         case 2:
#             lugar_para_cancelar = int(input('Qual lugar você gostaria de cancelar? '))
               
#             print(aniversario.cancelar_reserva(lugar_para_cancelar))
        
#         case 3:
#             print('===' * 4)
#             print(aniversario.show_places_disponiveis())
        
#         case 4:
#             break
        
#         case '_':
#             print('Opção inválida')
           