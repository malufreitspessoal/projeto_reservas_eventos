'''

Conexão com meu BD

'''

import sqlite3 as sql
import os

caminho_db =  os.path.join(os.path.dirname(__file__), "eventlu.db")


try:
    # Conectar ao banco de dados em modo de leitura/escrita
    conn = sql.connect(caminho_db)
    
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS organizadores(
            id_organizador INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            cnpj VARCHAR(14) NOT NULL,
            email VARCHAR(255) NOT NULL
        )
    ''')    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes(
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            cpf_cliente VARCHAR(11) unique,
            email VARCHAR(255) NOT NULL ,
            data_nascimento VARCHAR(11) NOT NULL
        )
    ''')



except sql.Error as e:
    print(f'Erro no banco de dados: {e}')