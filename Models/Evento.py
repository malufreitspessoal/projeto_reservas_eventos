from datetime import datetime, date
from utilitarios.funcoes import modelar_data_atual


class Evento:
    eventos = []
    def __init__(self, nome_evento, descricao_do_evento, organizador, faixa_etaria, data_evento, horario):
         self.nome_evento = nome_evento
         self.descricao_do_evento = descricao_do_evento
         self.organizador = organizador
         self.faixa_etaria = faixa_etaria
         self.data_evento = data_evento
         self.horario = horario

    @staticmethod
    def criar_evento(nome_organizador):
        nome_evento = input('Nome do evento: ').strip().upper()
        descricao_evento = input('Descrição do evento: ').strip().upper()
        faixa_etaria = input('Faixa etária do evento: ').strip().upper()
        
        while True:
            try:
                data_evento = input('Data do evento: ').strip()
                data_reformada = modelar_data_atual(data_evento).date() # saída ta datetime.date(2028, 3, 12)
                # data_reformada = data_objeto.date()
                data_atual = date.today()
                
                if data_atual > data_reformada:
                    print('Data não pode ser maior que o dia atual')
                
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.") 
            horario = input('Horário do evento: ')
            novo_evento = Evento(nome_evento, descricao_evento, nome_organizador , faixa_etaria, data_reformada, horario)
            Evento.eventos.append({
                'nome_evento': novo_evento.nome_evento,
                'descricao_evento': novo_evento.descricao_do_evento,
                'organizador': nome_organizador,
                'faixa_etaria': novo_evento.faixa_etaria,
                'data_evento': data_reformada,
                'horario': horario
                            })
            print('Evento criado com sucesso')
            print(Evento.eventos)
            return novo_evento