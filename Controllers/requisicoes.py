'''
Requisições ao meu BD
'''

'''
Tabelas:


Evento / Valor


Reserva

Venda



'''
from conexao import *
import sqlite3 as sql
import os
from Models.Cliente import Cliente



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

def cadastrar_cliente(obj:Cliente):
    query= f'''INSERT INTO `professores` (`nome`, `idade`, `cpf`, `telefone`, `sexo`, `formacao`, `valorHora`)
    VALUES(
            "{obj.nome}",
            "{obj.cpf}",
            "{obj.email}",
            "{obj.data_nascimento}")'''
    conn = sql.connect(caminho_db)
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        conn.commit()
        print('Registro inserido com sucesso!')
        input('')  
        
    except Exception as error:
        raise error('Deu ruim')
    else:
        pass

def cadastrar_organizador():
    pass