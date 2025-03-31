from datetime import datetime

def mostrar_menu_reservas():
     
    print()
    print('-- Menu --')
    print('===' * 4)
    print('1 - Reservar um lugar')
    print('2- Cancelar sua reserva')
    print('3- Exibir os lugares disponíveis')
    print('4- Sair')
    print()
    return  int(input('Sua opção: '))

def colunas():
    print( '---' * 5)


        

def modelar_data_atual():
    data = datetime.now()
    data_alterada = data.strftime('%d/%m/%Y %H:%M:%S')
    return(data_alterada)



print(modelar_data_atual())