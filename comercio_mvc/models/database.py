import sqlite3
from sqlite3 import Error

def criar_conexao(db_file):
    """Cria uma conexão com o banco de dados SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Conexão com SQLite estabelecida: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    
    return conn

def criar_tabelas(conn):
    """Cria as tabelas necessárias no banco de dados"""
    try:
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE,
            telefone TEXT
        );
        """)
        
        conn.commit()
    except Error as e:
        print(e)