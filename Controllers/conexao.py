'''

Conexão com meu BD

'''

import sqlite3 as sql
import os

caminho_db =  os.path.join(os.path.dirname(__file__), "eventlu.db")

conn = sql.connect(caminho_db)
    
cursor = conn.cursor()
