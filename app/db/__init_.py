import sqlite3

def get_db_connection():
    # Conexão com o banco de dados SQLite
    conn = sqlite3.connect('agenda.db')
    conn.row_factory = sqlite3.Row
    return conn
