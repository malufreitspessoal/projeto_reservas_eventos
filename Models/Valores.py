from Evento import Evento
from utilitarios.funcoes import colunas
# composição entre as classes.

class Valores:
    def __init__(self, evento, setor_pista, setor_arquibancada):
        self.evento = evento  # Instância de Evento
        self.setor_pista = setor_pista
        self.setor_arquibancada = setor_arquibancada


    def __repr__(self):
        faixa_etaria = f"{self.evento.faixa_etaria} anos" if self.evento.faixa_etaria != "Livre" else "Livre"
        return (f"""
        {self.evento.nome_evento} 
        Organizadores: {self.evento.organizador}.
        {self.evento.descricao_do_evento}.
        
        {colunas()} Valores {colunas()}
        Pista: R$ {self.setor_pista:.2f}
        Arquibancada: R$ {self.setor_arquibancada:.2f}
        Classificação {faixa_etaria}
        
    """)
    
    def definir_valores(self, quantidade_pista, quantidade_arquibancada):
        pass


evento = Evento('Festa', 'Lorem....', "Malu", '18')
valores = Valores(evento, 299.99, 99.99)

print(valores)