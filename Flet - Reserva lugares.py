import flet as ft

class Evento:
    def __init__(self, quantidade_de_lugares: int):
        self.quantidade_de_lugares = []
        self.lugares_reservados = []
        for i in range(1, quantidade_de_lugares + 1):
            self.quantidade_de_lugares.append(i)

    def reservar_lugar(self, lugar_reservado: int) -> str:
        if not self.quantidade_de_lugares:
            return 'Não há lugares disponíveis'

        if lugar_reservado in self.quantidade_de_lugares:
            self.quantidade_de_lugares.remove(lugar_reservado)
            self.lugares_reservados.append(lugar_reservado)
            self.lugares_reservados.sort()
            return f'Lugar {lugar_reservado} reservado com sucesso'

        elif lugar_reservado in self.lugares_reservados:
            return f'Lugar {lugar_reservado} já está reservado'

        else:
            return f'Lugar inexistente'

    def cancelar_reserva(self, lugar_cancelado: int) -> str:
        if lugar_cancelado in self.lugares_reservados:
            self.lugares_reservados.remove(lugar_cancelado)
            self.quantidade_de_lugares.append(lugar_cancelado)
            self.quantidade_de_lugares.sort()
            return f'Lugar {lugar_cancelado} cancelado com sucesso'

        elif lugar_cancelado in self.quantidade_de_lugares:
            return f'Esse lugar não foi reservado'

    def show_places_disponiveis(self) -> str:
        if not self.quantidade_de_lugares:
            return 'Não há mais lugares disponíveis'
        return f'Os lugares disponíveis são {self.quantidade_de_lugares}'


def main(page: ft.Page):
    page.title = "Sistema de Reservas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    evento = Evento(10)

    def reservar_lugar(e):
        try:
            lugar = int(lugar_reserva_input.value)
            resultado = evento.reservar_lugar(lugar)
            resultado_text.value = resultado
            lugares_disponiveis_text.value = evento.show_places_disponiveis()
        except ValueError:
            resultado_text.value = "Por favor, insira um número válido."
        page.update()

    def cancelar_reserva(e):
        try:
            lugar = int(lugar_cancelar_input.value)
            resultado = evento.cancelar_reserva(lugar)
            resultado_text.value = resultado
            lugares_disponiveis_text.value = evento.show_places_disponiveis()
        except ValueError:
            resultado_text.value = "Por favor, insira um número válido."
        page.update()

    def exibir_lugares_disponiveis(e):
        lugares_disponiveis_text.value = evento.show_places_disponiveis()
        page.update()

    # Componentes da interface
    lugar_reserva_input = ft.TextField(label="Número do lugar para reservar", width=300)
    reservar_button = ft.ElevatedButton(text="Reservar Lugar", on_click=reservar_lugar)

    lugar_cancelar_input = ft.TextField(label="Número do lugar para cancelar", width=300)
    cancelar_button = ft.ElevatedButton(text="Cancelar Reserva", on_click=cancelar_reserva)

    exibir_button = ft.ElevatedButton(text="Exibir Lugares Disponíveis", on_click=exibir_lugares_disponiveis)

    resultado_text = ft.Text(value="", size=16, color=ft.colors.BLUE)
    lugares_disponiveis_text = ft.Text(value=evento.show_places_disponiveis(), size=16, color=ft.colors.GREEN)

    # Adicionando componentes à página
    page.add(
        ft.Column(
            [
                ft.Text("Sistema de Reservas de Lugares", size=24, weight=ft.FontWeight.BOLD),
                lugar_reserva_input,
                reservar_button,
                lugar_cancelar_input,
                cancelar_button,
                exibir_button,
                resultado_text,
                lugares_disponiveis_text,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)