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
    return  ( '---' * 5)


        

def modelar_data_atual(data_string):
    """Converte uma string de data no formato dd/mm/aaaa para um objeto datetime.date."""
    try:
        data_objeto = datetime.strptime(data_string, "%d/%m/%Y")
        return data_objeto.strftime("%d/%m/%Y")  # Retorna a data formatada como string
    except ValueError:
        return None  # Retorna None em caso de erro

# print(modelar_data_atual("12/03/1997"))